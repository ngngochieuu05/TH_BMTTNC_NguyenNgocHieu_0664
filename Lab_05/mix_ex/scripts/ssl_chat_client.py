import socket
import ssl
import threading

from mix_portal.console_utf8 import configure_console_utf8


def main():
    configure_console_utf8()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    ssl_socket = context.wrap_socket(client_socket, server_hostname="localhost")
    ssl_socket.connect(("127.0.0.1", 12346))

    def receive_data():
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode("utf-8"))

    threading.Thread(target=receive_data, daemon=True).start()

    try:
        while True:
            message = input("Nhập tin nhắn: ")
            ssl_socket.send(message.encode("utf-8"))
    except KeyboardInterrupt:
        pass
    finally:
        ssl_socket.close()


if __name__ == "__main__":
    main()
