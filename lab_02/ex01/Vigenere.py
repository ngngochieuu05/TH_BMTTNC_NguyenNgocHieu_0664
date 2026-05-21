def format_key(key):
    return "".join(char.lower() for char in key if char.isalpha())


def shift_char(char, shift):
    ascii_offset = ord("A") if char.isupper() else ord("a")
    return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)


def encrypt(plain_text, key):
    key = format_key(key)
    cipher_text = ""
    key_index = 0

    if not key:
        return plain_text

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("a")
            cipher_text += shift_char(char, shift)
            key_index += 1
        else:
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, key):
    key = format_key(key)
    plain_text = ""
    key_index = 0

    if not key:
        return cipher_text

    for char in cipher_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord("a")
            plain_text += shift_char(char, -shift)
            key_index += 1
        else:
            plain_text += char

    return plain_text


def main():
    plain_text = input("Nhap chuoi can ma hoa: ")
    key = input("Nhap khoa: ")

    cipher_text = encrypt(plain_text, key)
    print("Chuoi da ma hoa:", cipher_text)

    decrypted_text = decrypt(cipher_text, key)
    print("Chuoi da giai ma:", decrypted_text)


if __name__ == "__main__":
    main()
