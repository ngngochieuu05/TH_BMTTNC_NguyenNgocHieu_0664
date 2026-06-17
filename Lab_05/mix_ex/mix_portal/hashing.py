import hashlib

from Crypto.Hash import SHA3_256


def compute_hash(algorithm: str, text: str):
    payload = text.encode("utf-8")
    algorithm = algorithm.lower()
    if algorithm == "md5":
        return hashlib.md5(payload).hexdigest()
    if algorithm == "sha256":
        return hashlib.sha256(payload).hexdigest()
    if algorithm == "sha3_256":
        digest = SHA3_256.new()
        digest.update(payload)
        return digest.hexdigest()
    if algorithm == "blake2b":
        return hashlib.blake2b(payload, digest_size=64).hexdigest()
    raise ValueError("Unsupported hash algorithm")
