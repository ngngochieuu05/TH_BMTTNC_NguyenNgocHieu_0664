from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayfairCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
from cipher.vigenere import VigenereCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()
vigenere_cipher = VigenereCipher()
playfair_cipher = PlayfairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()


def parse_json():
    return request.get_json(silent=True) or {}


def parse_caesar_key(data):
    try:
        return int(data["key"])
    except (KeyError, TypeError, ValueError):
        raise ValueError("Key must be an integer")


def parse_railfence_key(data):
    try:
        return int(data["key"])
    except (KeyError, TypeError, ValueError):
        raise ValueError("Key must be an integer")


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


@app.route("/api/playfair/encrypt", methods=["POST"])
def playfair_encrypt():
    try:
        data = parse_json()
        plain_text = data["plain_text"]
        key = data["key"]
        encrypted_text = playfair_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_text": encrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


@app.route("/api/playfair/decrypt", methods=["POST"])
def playfair_decrypt():
    try:
        data = parse_json()
        encrypted_text = data["encrypted_text"]
        key = data["key"]
        decrypted_text = playfair_cipher.decrypt_text(encrypted_text, key)
        return jsonify({"decrypted_text": decrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


@app.route("/api/railfence/encrypt", methods=["POST"])
def railfence_encrypt():
    try:
        data = parse_json()
        plain_text = data["plain_text"]
        key = parse_railfence_key(data)
        encrypted_text = railfence_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_text": encrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/railfence/decrypt", methods=["POST"])
def railfence_decrypt():
    try:
        data = parse_json()
        encrypted_text = data["encrypted_text"]
        key = parse_railfence_key(data)
        decrypted_text = railfence_cipher.decrypt_text(encrypted_text, key)
        return jsonify({"decrypted_text": decrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400
    except ValueError as error:
        return jsonify({"error": str(error)}), 400


@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    try:
        data = parse_json()
        plain_text = data["plain_text"]
        key = data["key"]
        encrypted_text = transposition_cipher.encrypt_text(plain_text, key)
        return jsonify({"encrypted_text": encrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    try:
        data = parse_json()
        encrypted_text = data["encrypted_text"]
        key = data["key"]
        decrypted_text = transposition_cipher.decrypt_text(encrypted_text, key)
        return jsonify({"decrypted_text": decrypted_text})
    except KeyError as error:
        return jsonify({"error": f"Missing field: {error.args[0]}"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
