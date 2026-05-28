from flask import Flask, request, render_template
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


@app.route("/caesar", methods=["GET", "POST"])
def caesar_page():
    form_data = {"action": "encrypt", "text": "", "key": ""}
    result = ""
    error = ""

    if request.method == "POST":
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                parsed_key = int(form_data["key"])
                if form_data["action"] == "encrypt":
                    result = caesar_cipher.encrypt_text(form_data["text"], parsed_key)
                else:
                    result = caesar_cipher.decrypt_text(form_data["text"], parsed_key)
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "caesar.html",
        form_data=form_data,
        result=result,
        error=error,
    )


@app.route("/vigenere", methods=["GET", "POST"])
def vigenere_page():
    form_data = {"action": "encrypt", "text": "", "key": ""}
    result = ""
    error = ""

    if request.method == "POST":
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                if form_data["action"] == "encrypt":
                    result = vigenere_cipher.encrypt_text(form_data["text"], form_data["key"])
                else:
                    result = vigenere_cipher.decrypt_text(form_data["text"], form_data["key"])
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "vigenere.html",
        form_data=form_data,
        result=result,
        error=error,
    )


@app.route("/playfair", methods=["GET", "POST"])
def playfair_page():
    form_data = {"action": "encrypt", "text": "", "key": ""}
    result = ""
    error = ""

    if request.method == "POST":
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                if form_data["action"] == "encrypt":
                    result = playfair_cipher.encrypt_text(form_data["text"], form_data["key"])
                else:
                    result = playfair_cipher.decrypt_text(form_data["text"], form_data["key"])
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "playfair.html",
        form_data=form_data,
        result=result,
        error=error,
    )


@app.route("/railfence", methods=["GET", "POST"])
def railfence_page():
    form_data = {"action": "encrypt", "text": "", "key": ""}
    result = ""
    error = ""

    if request.method == "POST":
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                parsed_key = int(form_data["key"])
                if form_data["action"] == "encrypt":
                    result = railfence_cipher.encrypt_text(form_data["text"], parsed_key)
                else:
                    result = railfence_cipher.decrypt_text(form_data["text"], parsed_key)
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "railfence.html",
        form_data=form_data,
        result=result,
        error=error,
    )


@app.route("/transposition", methods=["GET", "POST"])
def transposition_page():
    form_data = {"action": "encrypt", "text": "", "key": ""}
    result = ""
    error = ""

    if request.method == "POST":
        form_data["action"] = request.form.get("action", "encrypt")
        form_data["text"] = request.form.get("text", "")
        form_data["key"] = request.form.get("key", "").strip()

        if not form_data["text"]:
            error = "Vui long nhap noi dung can xu ly."
        elif not form_data["key"]:
            error = "Vui long nhap khoa."
        else:
            try:
                if form_data["action"] == "encrypt":
                    result = transposition_cipher.encrypt_text(form_data["text"], form_data["key"])
                else:
                    result = transposition_cipher.decrypt_text(form_data["text"], form_data["key"])
            except ValueError as exc:
                error = str(exc)
            except Exception as exc:
                error = f"Khong the xu ly yeu cau: {exc}"

    return render_template(
        "transposition.html",
        form_data=form_data,
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
