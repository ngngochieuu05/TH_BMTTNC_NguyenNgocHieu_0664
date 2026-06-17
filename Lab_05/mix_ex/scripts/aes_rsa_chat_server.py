import socket
import threading

from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from mix_portal.console_utf8 import configure_console_utf8


clients = []
server_key = RSA.generate(2048)


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    return cipher.iv + cipher.encrypt(pad(message.encode(), AES.block_size))


def decrypt_message(key, payload):
    iv = payload[: AES.block_size]
    ciphertext = payload[AES.block_size :]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()


def handle_client(client_socket, address):
    print(f"Đã kết nối: {address}")
    client_socket.send(server_key.publickey().export_key(format="PEM"))
    client_public = RSA.import_key(client_socket.recv(2048))
    aes_key = get_random_bytes(16)
    client_socket.send(PKCS1_OAEP.new(client_public).encrypt(aes_key))
    clients.append((client_socket, aes_key))

    try:
        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                break
            message = decrypt_message(aes_key, encrypted_message)
            print(f"{address}: {message}")
            for client, key in clients:
                if client != client_socket:
                    client.send(encrypt_message(key, message))
            if message.lower() == "exit":
                break
    finally:
        clients.remove((client_socket, aes_key))
        client_socket.close()
        print(f"Đã ngắt kết nối: {address}")


def main():
    configure_console_utf8()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)
    print("Server chat AES/RSA đang lắng nghe tại 127.0.0.1:12345")
    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, address), daemon=True).start()


if __name__ == "__main__":
    main()
