import socket
import ssl
import threading
from pathlib import Path

from mix_portal.console_utf8 import configure_console_utf8


clients = []


def handle_client(client_socket):
    print("Đã kết nối:", client_socket.getpeername())
    try:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))
            for client in list(clients):
                if client != client_socket:
                    try:
                        client.send(data)
                    except OSError:
                        clients.remove(client)
    finally:
        if client_socket in clients:
            clients.remove(client_socket)
        print("Đã ngắt kết nối:", client_socket.getpeername())
        client_socket.close()


def main():
    configure_console_utf8()
    cert_dir = Path(__file__).resolve().parents[1] / "mix_portal" / "certificates"
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile=str(cert_dir / "server-cert.crt"),
        keyfile=str(cert_dir / "server-key.key"),
    )

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12346))
    server_socket.listen(5)
    print("Server chat SSL đang lắng nghe tại 127.0.0.1:12346")

    while True:
        client_socket, _ = server_socket.accept()
        ssl_socket = context.wrap_socket(client_socket, server_side=True)
        clients.append(ssl_socket)
        threading.Thread(target=handle_client, args=(ssl_socket,), daemon=True).start()


if __name__ == "__main__":
    main()
