import socket
import threading

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from mix_portal.console_utf8 import configure_console_utf8


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(message.encode(), AES.block_size))


def decrypt_message(key, payload):
    iv = payload[: AES.block_size]
    ciphertext = payload[AES.block_size :]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()


def main():
    configure_console_utf8()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))

    client_key = RSA.generate(2048)
    server_public = RSA.import_key(client_socket.recv(2048))
    client_socket.send(client_key.publickey().export_key(format="PEM"))
    encrypted_aes_key = client_socket.recv(2048)
    aes_key = PKCS1_OAEP.new(client_key).decrypt(encrypted_aes_key)

    def receive_messages():
        while True:
            payload = client_socket.recv(1024)
            if not payload:
                break
            print("Nhận:", decrypt_message(aes_key, payload))

    threading.Thread(target=receive_messages, daemon=True).start()

    while True:
        message = input("Nhập tin nhắn ('exit' để thoát): ")
        client_socket.send(encrypt_message(aes_key, message))
        if message.lower() == "exit":
            break

    client_socket.close()


if __name__ == "__main__":
    main()
