def shift_char(char, shift):
    ascii_offset = ord("A") if char.isupper() else ord("a")
    return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)


def encrypt(plain_text, shift):
    cipher_text = ""

    for char in plain_text:
        if char.isalpha():
            cipher_text += shift_char(char, shift)
        else:
            cipher_text += char

    return cipher_text


def decrypt(cipher_text, shift):
    plain_text = ""

    for char in cipher_text:
        if char.isalpha():
            plain_text += shift_char(char, -shift)
        else:
            plain_text += char

    return plain_text


def main():
    plain_text = input("Nhap chuoi can ma hoa: ")
    shift = int(input("Nhap so luong ky tu can dich: "))

    cipher_text = encrypt(plain_text, shift)
    print("Chuoi da ma hoa:", cipher_text)

    decrypted_text = decrypt(cipher_text, shift)
    print("Chuoi da giai ma:", decrypted_text)


if __name__ == "__main__":
    main()
