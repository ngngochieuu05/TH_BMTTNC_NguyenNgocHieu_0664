import os
import sys
import json

from flask import Flask, request, jsonify

try:
    from cipher.rsa import RSACipher
except ImportError:
    RSACipher = None
from cipher.ecc import ECCCipher

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "lab_02", "ex01_API")))
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()

# RSA CIPHER ALGORITHM
rsa_cipher = RSACipher() if RSACipher is not None else None
ecc_cipher = ECCCipher()


def parse_json():
    return request.get_json(silent=True) or {}


def parse_caesar_key(data):
    try:
        return int(data["key"])
    except (KeyError, TypeError, ValueError):
        raise ValueError("Key must be an integer")


def require_rsa_cipher():
    if rsa_cipher is None:
        return jsonify({"error": "RSA cipher implementation is unavailable"}), 500
    return None


def handle_missing_keys(error):
    return jsonify({"error": f"Key file not found: {error.filename}"}), 400


@app.route("/caesar/encrypt", methods=["POST"])
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    try:
        data = parse_json()
        plain_text = data["plain_text"]
        key = parse_caesar_key(data)
        encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_text": encrypted_text})
    except KeyError:
        return jsonify({"error": "Missing field: plain_text"}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/caesar/decrypt", methods=["POST"])
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    try:
        data = parse_json()
        encrypted_text = data["encrypted_text"]
        key = parse_caesar_key(data)
        decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
        return jsonify({"decrypted_text": decrypted_text})
    except KeyError:
        return jsonify({"error": "Missing field: encrypted_text"}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/vigenere/encrypt", methods=["POST"])
@app.route("/api/vigenere/encrypt", methods=["POST"])
def vigenere_encrypt():
    try:
        data = parse_json()
        plain_text = data["plain_text"]
        key = data["key"]
        encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_text": encrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


@app.route("/vigenere/decrypt", methods=["POST"])
@app.route("/api/vigenere/decrypt", methods=["POST"])
def vigenere_decrypt():
    try:
        data = parse_json()
        encrypted_text = data["encrypted_text"]
        key = data["key"]
        decrypted_text = vigenere_cipher.decrypt_text(encrypted_text, key)
        return jsonify({"decrypted_text": decrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


@app.route("/api/rsa/generate_keys", methods=["GET"])
def rsa_generate_keys():
    rsa_error = require_rsa_cipher()
    if rsa_error is not None:
        return rsa_error
    rsa_cipher.generate_keys()
    return jsonify({"message": "Keys generated successfully"})


@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    rsa_error = require_rsa_cipher()
    if rsa_error is not None:
        return rsa_error
    data = request.json

    message = data["message"]
    key_type = data["key_type"]

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == "public":
        key = public_key
    elif key_type == "private":
        key = private_key
    else:
        return jsonify({"error": "Invalid key type"})

    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()

    return jsonify({"encrypted_message": encrypted_hex})


@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    rsa_error = require_rsa_cipher()
    if rsa_error is not None:
        return rsa_error
    data = request.json

    ciphertext_hex = data["ciphertext"]
    key_type = data["key_type"]

    private_key, public_key = rsa_cipher.load_keys()

    if key_type == "public":
        key = public_key
    elif key_type == "private":
        key = private_key
    else:
        return jsonify({"error": "Invalid key type"})

    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)

    return jsonify({"decrypted_message": decrypted_message})


@app.route("/api/rsa/sign", methods=["POST"])
def rsa_sign_message():
    rsa_error = require_rsa_cipher()
    if rsa_error is not None:
        return rsa_error
    data = request.json

    message = data["message"]

    private_key, public_key = rsa_cipher.load_keys()

    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()

    return jsonify({"signature": signature_hex})


@app.route("/api/rsa/verify", methods=["POST"])
def rsa_verify_signature():
    rsa_error = require_rsa_cipher()
    if rsa_error is not None:
        return rsa_error
    data = request.json

    message = data["message"]
    signature_hex = data["signature"]

    private_key, public_key = rsa_cipher.load_keys()

    signature = bytes.fromhex(signature_hex)

    is_verified = rsa_cipher.verify(message, signature, public_key)

    return jsonify({"is_verified": is_verified})


@app.route("/api/ecc/generate_keys", methods=["GET"])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({"message": "ECC keys generated successfully"})


@app.route("/api/ecc/encrypt", methods=["POST"])
def ecc_encrypt():
    try:
        data = parse_json()
        message = data["message"]
        _, public_key = ecc_cipher.load_keys()
        encrypted_message = ecc_cipher.encrypt(message, public_key)
        return jsonify({"encrypted_message": encrypted_message})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except FileNotFoundError as error:
        return handle_missing_keys(error)
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/ecc/decrypt", methods=["POST"])
def ecc_decrypt():
    try:
        data = parse_json()
        encrypted_message = data["ciphertext"]
        private_key, _ = ecc_cipher.load_keys()
        decrypted_message = ecc_cipher.decrypt(encrypted_message, private_key)
        return jsonify({"decrypted_message": decrypted_message})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except FileNotFoundError as error:
        return handle_missing_keys(error)
    except (ValueError, json.JSONDecodeError) as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/ecc/sign", methods=["POST"])
def ecc_sign_message():
    try:
        data = parse_json()
        message = data["message"]
        private_key, _ = ecc_cipher.load_keys()
        signature = ecc_cipher.sign(message, private_key)
        return jsonify({"signature": signature})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except FileNotFoundError as error:
        return handle_missing_keys(error)


@app.route("/api/ecc/verify", methods=["POST"])
def ecc_verify_signature():
    try:
        data = parse_json()
        message = data["message"]
        signature = data["signature"]
        _, public_key = ecc_cipher.load_keys()
        is_verified = ecc_cipher.verify(message, signature, public_key)
        return jsonify({"is_verified": is_verified})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except FileNotFoundError as error:
        return handle_missing_keys(error)


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
