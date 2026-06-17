import base64
import hashlib
import json
import secrets
from dataclasses import dataclass
from pathlib import Path

import rsa


class RSACipher:
    def __init__(self, key_dir: Path):
        key_dir.mkdir(parents=True, exist_ok=True)
        self.private_key_path = key_dir / "rsa_private_key.pem"
        self.public_key_path = key_dir / "rsa_public_key.pem"
        if not self.private_key_path.exists() or not self.public_key_path.exists():
            self.generate_keys()

    def generate_keys(self):
        public_key, private_key = rsa.newkeys(1024)
        self.private_key_path.write_bytes(private_key.save_pkcs1("PEM"))
        self.public_key_path.write_bytes(public_key.save_pkcs1("PEM"))

    def load_keys(self):
        private_key = rsa.PrivateKey.load_pkcs1(self.private_key_path.read_bytes())
        public_key = rsa.PublicKey.load_pkcs1(self.public_key_path.read_bytes())
        return private_key, public_key

    def encrypt(self, message: str) -> str:
        _, public_key = self.load_keys()
        return rsa.encrypt(message.encode("utf-8"), public_key).hex()

    def decrypt(self, ciphertext_hex: str) -> str:
        private_key, _ = self.load_keys()
        return rsa.decrypt(bytes.fromhex(ciphertext_hex), private_key).decode("utf-8")

    def sign(self, message: str) -> str:
        private_key, _ = self.load_keys()
        return rsa.sign(message.encode("utf-8"), private_key, "SHA-256").hex()

    def verify(self, message: str, signature_hex: str) -> bool:
        _, public_key = self.load_keys()
        try:
            rsa.verify(message.encode("utf-8"), bytes.fromhex(signature_hex), public_key)
            return True
        except rsa.VerificationError:
            return False


@dataclass(frozen=True)
class CurvePoint:
    x: int
    y: int


class ECCCipher:
    P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    A = 0
    B = 7
    N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
    G = CurvePoint(
        55066263022277343669578718895168534326250603453777594175500187360389116729240,
        32670510020758816978083085130507043184471273380659243275938904335757337482424,
    )

    def __init__(self, key_dir: Path):
        key_dir.mkdir(parents=True, exist_ok=True)
        self.private_key_path = key_dir / "ecc_private_key.pem"
        self.public_key_path = key_dir / "ecc_public_key.pem"
        self._byte_len = (self.P.bit_length() + 7) // 8
        if not self.private_key_path.exists() or not self.public_key_path.exists():
            self.generate_keys()

    def inverse_mod(self, value: int, modulus: int) -> int:
        return pow(value, -1, modulus)

    def point_add(self, p1, p2):
        if p1 is None:
            return p2
        if p2 is None:
            return p1
        if p1.x == p2.x and (p1.y != p2.y or p1.y == 0):
            return None
        if p1 == p2:
            slope = (3 * p1.x * p1.x + self.A) * self.inverse_mod(2 * p1.y % self.P, self.P)
        else:
            slope = (p2.y - p1.y) * self.inverse_mod((p2.x - p1.x) % self.P, self.P)
        slope %= self.P
        x3 = (slope * slope - p1.x - p2.x) % self.P
        y3 = (slope * (p1.x - x3) - p1.y) % self.P
        return CurvePoint(x3, y3)

    def scalar_mult(self, scalar: int, point):
        if scalar % self.N == 0 or point is None:
            return None
        result = None
        addend = point
        while scalar:
            if scalar & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            scalar >>= 1
        return result

    def _write_pem(self, path: Path, header: str, raw_bytes: bytes):
        b64 = base64.b64encode(raw_bytes).decode("ascii")
        lines = [f"-----BEGIN {header}-----"]
        lines.extend(b64[index : index + 64] for index in range(0, len(b64), 64))
        lines.append(f"-----END {header}-----")
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def _read_pem(self, path: Path) -> bytes:
        lines = [line for line in path.read_text(encoding="utf-8").splitlines() if not line.startswith("-----")]
        return base64.b64decode("".join(lines))

    def generate_keys(self):
        private_key = secrets.randbelow(self.N - 1) + 1
        public_key = self.scalar_mult(private_key, self.G)
        self._write_pem(
            self.private_key_path,
            "ECC PRIVATE KEY",
            private_key.to_bytes(self._byte_len, "big"),
        )
        raw_public = (
            b"\x04"
            + public_key.x.to_bytes(self._byte_len, "big")
            + public_key.y.to_bytes(self._byte_len, "big")
        )
        self._write_pem(self.public_key_path, "ECC PUBLIC KEY", raw_public)

    def load_keys(self):
        private_key = int.from_bytes(self._read_pem(self.private_key_path), "big")
        raw_public = self._read_pem(self.public_key_path)
        x = int.from_bytes(raw_public[1 : 1 + self._byte_len], "big")
        y = int.from_bytes(raw_public[1 + self._byte_len :], "big")
        return private_key, CurvePoint(x, y)

    def derive_keystream(self, shared_secret: int, length: int) -> bytes:
        seed = shared_secret.to_bytes(32, "big")
        stream = bytearray()
        counter = 0
        while len(stream) < length:
            stream.extend(hashlib.sha256(seed + counter.to_bytes(4, "big")).digest())
            counter += 1
        return bytes(stream[:length])

    def encrypt(self, message: str) -> str:
        _, public_key = self.load_keys()
        plaintext = message.encode("utf-8")
        ephemeral_private = secrets.randbelow(self.N - 1) + 1
        ephemeral_public = self.scalar_mult(ephemeral_private, self.G)
        shared_point = self.scalar_mult(ephemeral_private, public_key)
        keystream = self.derive_keystream(shared_point.x, len(plaintext))
        ciphertext = bytes(a ^ b for a, b in zip(plaintext, keystream))
        payload = {
            "ephemeral_public_key": {"x": str(ephemeral_public.x), "y": str(ephemeral_public.y)},
            "ciphertext": ciphertext.hex(),
        }
        return base64.b64encode(json.dumps(payload).encode("utf-8")).decode("ascii")

    def decrypt(self, encrypted_message: str) -> str:
        private_key, _ = self.load_keys()
        payload = json.loads(base64.b64decode(encrypted_message.encode("ascii")).decode("utf-8"))
        ephemeral_public_key = CurvePoint(
            int(payload["ephemeral_public_key"]["x"]),
            int(payload["ephemeral_public_key"]["y"]),
        )
        ciphertext = bytes.fromhex(payload["ciphertext"])
        shared_point = self.scalar_mult(private_key, ephemeral_public_key)
        keystream = self.derive_keystream(shared_point.x, len(ciphertext))
        plaintext = bytes(a ^ b for a, b in zip(ciphertext, keystream))
        return plaintext.decode("utf-8")

    def sign(self, message: str) -> str:
        private_key, _ = self.load_keys()
        z = int.from_bytes(hashlib.sha256(message.encode("utf-8")).digest(), "big") % self.N
        while True:
            nonce = secrets.randbelow(self.N - 1) + 1
            point = self.scalar_mult(nonce, self.G)
            if point is None:
                continue
            r = point.x % self.N
            if r == 0:
                continue
            s = (self.inverse_mod(nonce, self.N) * (z + r * private_key)) % self.N
            if s != 0:
                return f"{r:064x}{s:064x}"

    def verify(self, message: str, signature: str) -> bool:
        _, public_key = self.load_keys()
        if len(signature) != 128:
            return False
        try:
            r = int(signature[:64], 16)
            s = int(signature[64:], 16)
        except ValueError:
            return False
        if not (1 <= r < self.N and 1 <= s < self.N):
            return False
        z = int.from_bytes(hashlib.sha256(message.encode("utf-8")).digest(), "big") % self.N
        s_inv = self.inverse_mod(s, self.N)
        u1 = (z * s_inv) % self.N
        u2 = (r * s_inv) % self.N
        point = self.point_add(self.scalar_mult(u1, self.G), self.scalar_mult(u2, public_key))
        return point is not None and point.x % self.N == r
