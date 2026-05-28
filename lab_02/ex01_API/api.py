from flask import Flask, request, jsonify, render_template
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

CIPHER_OPTIONS = [
    ("caesar", "Caesar"),
    ("vigenere", "Vigenere"),
    ("playfair", "Playfair"),
    ("railfence", "Rail Fence"),
    ("transposition", "Transposition"),
]


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


def process_cipher_request(algorithm: str, action: str, text: str, key: str):
    if algorithm == "caesar":
        parsed_key = int(key)
        if action == "encrypt":
            return caesar_cipher.encrypt_text(text, parsed_key)
        return caesar_cipher.decrypt_text(text, parsed_key)

    if algorithm == "vigenere":
        if action == "encrypt":
            return vigenere_cipher.encrypt_text(text, key)
        return vigenere_cipher.decrypt_text(text, key)

    if algorithm == "playfair":
        if action == "encrypt":
            return playfair_cipher.encrypt_text(text, key)
        return playfair_cipher.decrypt_text(text, key)

    if algorithm == "railfence":
        parsed_key = int(key)
        if action == "encrypt":
            return railfence_cipher.encrypt_text(text, parsed_key)
        return railfence_cipher.decrypt_text(text, parsed_key)

    if algorithm == "transposition":
        if action == "encrypt":
            return transposition_cipher.encrypt_text(text, key)
        return transposition_cipher.decrypt_text(text, key)

    raise ValueError("Unsupported algorithm")


@app.route("/", methods=["GET", "POST"])
@app.route("/browser", methods=["GET", "POST"])
def browser():
    form_data = {
        "algorithm": "caesar",
        "action": "encrypt",
        "text": "",
        "key": "",
    }
    result = ""
    error = ""

    if request.method == "POST":
        form_data["algorithm"] = request.form.get("algorithm", "caesar")
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                result = process_cipher_request(
                    form_data["algorithm"],
                    form_data["action"],
                    form_data["text"],
                    form_data["key"],
                )
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "index.html",
        cipher_options=CIPHER_OPTIONS,
        form_data=form_data,
        result=result,
        error=error,
    )


@app.route("/caesar/encrypt", methods=["POST"])
@app.route("/api/caesar/encrypt", methods=["POST"])
def encrypt():
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
def decrypt():
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


@app.route("/playfair/encrypt", methods=["POST"])
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


@app.route("/playfair/decrypt", methods=["POST"])
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


@app.route("/railfence/encrypt", methods=["POST"])
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


@app.route("/railfence/decrypt", methods=["POST"])
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


@app.route("/transposition/encrypt", methods=["POST"])
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


@app.route("/transposition/decrypt", methods=["POST"])
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
    app.run(host="0.0.0.0", port=5000, debug=True)
