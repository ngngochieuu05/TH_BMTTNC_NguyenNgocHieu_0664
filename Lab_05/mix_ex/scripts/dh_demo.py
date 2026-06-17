from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh

from mix_portal.console_utf8 import configure_console_utf8


def main():
    configure_console_utf8()
    parameters = dh.generate_parameters(generator=2, key_size=2048)
    server_private = parameters.generate_private_key()
    server_public = server_private.public_key()

    client_private = parameters.generate_private_key()
    client_public = client_private.public_key()

    server_secret = server_private.exchange(client_public)
    client_secret = client_private.exchange(server_public)

    print("Khóa công khai phía server:")
    print(
        server_public.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")
    )
    print("Bí mật chung phía server:", server_secret.hex())
    print("Bí mật chung phía client:", client_secret.hex())
    print("Hai bên khớp khóa chung:", server_secret == client_secret)


if __name__ == "__main__":
    main()
