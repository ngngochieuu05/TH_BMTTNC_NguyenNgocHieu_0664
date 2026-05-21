class VigenereCipher:
    @staticmethod
    def format_key(key):
        return "".join(char.lower() for char in key if char.isalpha())

    @staticmethod
    def shift_char(char, shift):
        ascii_offset = ord("A") if char.isupper() else ord("a")
        return chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)

    def encrypt_text(self, plain_text, key):
        key = self.format_key(key)
        cipher_text = ""
        key_index = 0

        if not key:
            return plain_text

        for char in plain_text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord("a")
                cipher_text += self.shift_char(char, shift)
                key_index += 1
            else:
                cipher_text += char

        return cipher_text

    def decrypt_text(self, cipher_text, key):
        key = self.format_key(key)
        plain_text = ""
        key_index = 0

        if not key:
            return cipher_text

        for char in cipher_text:
            if char.isalpha():
                shift = ord(key[key_index % len(key)]) - ord("a")
                plain_text += self.shift_char(char, -shift)
                key_index += 1
            else:
                plain_text += char

        return plain_text
