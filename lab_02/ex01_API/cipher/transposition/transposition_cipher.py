class TranspositionCipher:
    def __init__(self):
        pass

    def parse_key(self, key):
        try:
            parsed_key = int(key)
        except (TypeError, ValueError):
            raise ValueError("Key must be an integer")

        if parsed_key < 2:
            raise ValueError("Key must be greater than 1")

        return parsed_key

    def format_text(self, text: str):
        return ''.join(letter for letter in text.upper() if letter.isalpha())

    def create_matrix(self, text: str, key: int):
        rows = []

        for index in range(0, len(text), key):
            row = list(text[index:index + key])
            while len(row) < key:
                row.append('X')
            rows.append(row)

        return rows

    def encrypt_text(self, text: str, key):
        key = self.parse_key(key)
        text = self.format_text(text)

        matrix = self.create_matrix(text, key)
        encrypt_text = []

        for column in range(key):
            for row in matrix:
                encrypt_text.append(row[column])

        return ''.join(encrypt_text)

    def decrypt_text(self, text: str, key):
        key = self.parse_key(key)
        text = self.format_text(text)

        if len(text) % key != 0:
            raise ValueError("Encrypted text length is invalid for this key")

        row_count = len(text) // key
        matrix = [['' for _ in range(key)] for _ in range(row_count)]
        index = 0

        for column in range(key):
            for row in range(row_count):
                matrix[row][column] = text[index]
                index += 1

        decrypt_text = []

        for row in matrix:
            decrypt_text.extend(row)

        return ''.join(decrypt_text).rstrip('X')
