import base64
import io
import os
import queue
import random
import threading
import time
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_file
from flask_sock import Sock

from .algorithms import run_classical_cipher
from .basics import circle_area, even_sum, greeting, parity, reverse_text, to_tuple
from .blockchain_tools import Blockchain
from .hashing import compute_hash
from .modern import ECCCipher, RSACipher
from .steganography import decode_image, encode_image
from .students import StudentStore


WORDS = ["táo", "chuối", "cam", "nho", "dưa", "mật mã", "khối", "socket", "băm"]


def create_app():
    base_dir = Path(__file__).resolve().parent.parent
    app = Flask(
        __name__,
        template_folder=str(base_dir / "mix_portal" / "templates"),
        static_folder=str(base_dir / "mix_portal" / "static"),
    )
    sock = Sock(app)

    student_store = StudentStore(base_dir / "data" / "students.json")
    blockchain = Blockchain()
    rsa_cipher = RSACipher(base_dir / "mix_portal" / "keys")
    ecc_cipher = ECCCipher(base_dir / "mix_portal" / "keys")

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/api/overview")
    def overview():
        return jsonify(
            {
                "labs": {
                    "lab_01": ["nhập xuất cơ bản", "bài toán số học", "quản lý sinh viên"],
                    "lab_02": ["caesar", "vigenere", "playfair", "rail fence", "chuyển vị", "flask api"],
                    "lab_03": ["rsa", "ecc", "api endpoint", "chữ ký số"],
                    "lab_04": ["md5", "sha256", "sha3", "blake2", "diffie-hellman", "chat aes/rsa", "websocket"],
                    "lab_05": ["base64", "blockchain", "giấu tin trong ảnh", "ssl socket"],
                }
            }
        )

    @app.route("/api/basics/greet", methods=["POST"])
    def basics_greet():
        data = request.get_json(silent=True) or {}
        return jsonify({"message": greeting(data["name"], int(data["age"]))})

    @app.route("/api/basics/circle-area", methods=["POST"])
    def basics_circle_area():
        data = request.get_json(silent=True) or {}
        return jsonify({"area": circle_area(float(data["radius"]))})

    @app.route("/api/basics/parity", methods=["POST"])
    def basics_parity():
        data = request.get_json(silent=True) or {}
        return jsonify({"parity": parity(int(data["number"]))})

    @app.route("/api/basics/even-sum", methods=["POST"])
    def basics_even_sum():
        data = request.get_json(silent=True) or {}
        return jsonify({"sum": even_sum([int(value) for value in data["values"]])})

    @app.route("/api/basics/reverse", methods=["POST"])
    def basics_reverse():
        data = request.get_json(silent=True) or {}
        return jsonify({"reversed": reverse_text(data["text"])})

    @app.route("/api/basics/to-tuple", methods=["POST"])
    def basics_to_tuple():
        data = request.get_json(silent=True) or {}
        return jsonify({"tuple": list(to_tuple(data["values"]))})

    @app.route("/api/classical", methods=["POST"])
    def classical():
        data = request.get_json(silent=True) or {}
        result = run_classical_cipher(
            data["algorithm"],
            data["action"],
            data["text"],
            str(data["key"]),
        )
        return jsonify({"result": result})

    @app.route("/api/rsa/generate", methods=["POST"])
    def rsa_generate():
        rsa_cipher.generate_keys()
        return jsonify({"message": "Đã tạo khóa RSA"})

    @app.route("/api/rsa/encrypt", methods=["POST"])
    def rsa_encrypt():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": rsa_cipher.encrypt(data["message"])})

    @app.route("/api/rsa/decrypt", methods=["POST"])
    def rsa_decrypt():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": rsa_cipher.decrypt(data["ciphertext"])})

    @app.route("/api/rsa/sign", methods=["POST"])
    def rsa_sign():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": rsa_cipher.sign(data["message"])})

    @app.route("/api/rsa/verify", methods=["POST"])
    def rsa_verify():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": rsa_cipher.verify(data["message"], data["signature"])})

    @app.route("/api/ecc/generate", methods=["POST"])
    def ecc_generate():
        ecc_cipher.generate_keys()
        return jsonify({"message": "Đã tạo khóa ECC"})

    @app.route("/api/ecc/encrypt", methods=["POST"])
    def ecc_encrypt():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": ecc_cipher.encrypt(data["message"])})

    @app.route("/api/ecc/decrypt", methods=["POST"])
    def ecc_decrypt():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": ecc_cipher.decrypt(data["ciphertext"])})

    @app.route("/api/ecc/sign", methods=["POST"])
    def ecc_sign():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": ecc_cipher.sign(data["message"])})

    @app.route("/api/ecc/verify", methods=["POST"])
    def ecc_verify():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": ecc_cipher.verify(data["message"], data["signature"])})

    @app.route("/api/hash", methods=["POST"])
    def hash_api():
        data = request.get_json(silent=True) or {}
        return jsonify({"result": compute_hash(data["algorithm"], data["text"])})

    @app.route("/api/base64/encode", methods=["POST"])
    def base64_encode():
        data = request.get_json(silent=True) or {}
        encoded = base64.b64encode(data["text"].encode("utf-8")).decode("utf-8")
        return jsonify({"result": encoded})

    @app.route("/api/base64/decode", methods=["POST"])
    def base64_decode():
        data = request.get_json(silent=True) or {}
        decoded = base64.b64decode(data["text"]).decode("utf-8")
        return jsonify({"result": decoded})

    @app.route("/api/students", methods=["GET", "POST"])
    def students():
        if request.method == "GET":
            return jsonify(student_store.list_students())
        data = request.get_json(silent=True) or {}
        student = student_store.create_student(
            data["name"],
            data["sex"],
            data["major"],
            float(data["diem_tb"]),
        )
        return jsonify(student), 201

    @app.route("/api/students/<int:student_id>", methods=["PUT", "DELETE"])
    def student_detail(student_id: int):
        if request.method == "DELETE":
            student_store.delete_student(student_id)
            return jsonify({"message": "Đã xóa sinh viên"})
        data = request.get_json(silent=True) or {}
        student = student_store.update_student(
            student_id,
            data["name"],
            data["sex"],
            data["major"],
            float(data["diem_tb"]),
        )
        return jsonify(student)

    @app.route("/api/students/search")
    def student_search():
        return jsonify(student_store.search_by_name(request.args.get("q", "")))

    @app.route("/api/students/sort/name")
    def student_sort_name():
        return jsonify(student_store.sort_by_name())

    @app.route("/api/students/sort/score")
    def student_sort_score():
        return jsonify(student_store.sort_by_diem_tb())

    @app.route("/api/blockchain", methods=["GET"])
    def blockchain_state():
        return jsonify(blockchain.to_dict())

    @app.route("/api/blockchain/transactions", methods=["POST"])
    def blockchain_add_transaction():
        data = request.get_json(silent=True) or {}
        next_block = blockchain.add_transaction(data["sender"], data["receiver"], float(data["amount"]))
        return jsonify({"message": f"Giao dịch sẽ được thêm vào khối {next_block}"})

    @app.route("/api/blockchain/mine", methods=["POST"])
    def blockchain_mine():
        previous_block = blockchain.get_previous_block()
        proof = blockchain.proof_of_work(previous_block.proof)
        blockchain.add_transaction("System", "Miner", 1)
        block = blockchain.create_block(proof, previous_block.hash)
        return jsonify({"message": "Đã đào khối mới", "block": block.to_dict()})

    @app.route("/api/steganography/encode", methods=["POST"])
    def steganography_encode():
        image = request.files["image"]
        message = request.form["message"]
        upload_dir = base_dir / "mix_portal" / "uploads"
        source_path = upload_dir / f"source_{int(time.time())}_{image.filename}"
        output_path = upload_dir / f"encoded_{int(time.time())}.png"
        source_path.parent.mkdir(parents=True, exist_ok=True)
        image.save(source_path)
        encoded_path = encode_image(source_path, message, output_path)
        return send_file(encoded_path, as_attachment=True, download_name="encoded_image.png")

    @app.route("/api/steganography/decode", methods=["POST"])
    def steganography_decode():
        image = request.files["image"]
        upload_dir = base_dir / "mix_portal" / "uploads"
        source_path = upload_dir / f"decode_{int(time.time())}_{image.filename}"
        image.save(source_path)
        return jsonify({"result": decode_image(source_path)})

    @app.route("/api/scripts")
    def scripts():
        return jsonify(
            {
                "dh_demo": "python scripts/dh_demo.py",
                "aes_rsa_server": "python scripts/aes_rsa_chat_server.py",
                "aes_rsa_client": "python scripts/aes_rsa_chat_client.py",
                "ssl_server": "python scripts/ssl_chat_server.py",
                "ssl_client": "python scripts/ssl_chat_client.py",
                "web_app": "python app.py",
            }
        )

    @sock.route("/ws/random-words")
    def random_words(ws):
        while True:
            ws.send(random.choice(WORDS))
            time.sleep(3)

    @app.errorhandler(Exception)
    def handle_error(error):
        return jsonify({"error": str(error)}), 400

    return app
