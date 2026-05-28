class TranspositionCipher:
    def __init__(self):
        pass

    def format_key(self, key: str):
        return ''.join(letter for letter in key.upper() if letter.isalpha())

    def format_text(self, text: str):
        return ''.join(letter for letter in text.upper() if letter.isalpha())

    def get_column_order(self, key: str):
        return [index for index, _ in sorted(enumerate(key), key=lambda item: (item[1], item[0]))]

    def create_matrix(self, text: str, key: str):
        key_len = len(key)
        rows = []

        for index in range(0, len(text), key_len):
            row = list(text[index:index + key_len])
            while len(row) < key_len:
                row.append('X')
            rows.append(row)

        return rows

    def encrypt_text(self, text: str, key: str):
        key = self.format_key(key)
        text = self.format_text(text)

        if not key:
            return text

        matrix = self.create_matrix(text, key)
        column_order = self.get_column_order(key)
        encrypt_text = []

        for column in column_order:
            for row in matrix:
                encrypt_text.append(row[column])

        return ''.join(encrypt_text)

    def decrypt_text(self, text: str, key: str):
        key = self.format_key(key)
        text = self.format_text(text)

        if not key:
            return text

        key_len = len(key)
        row_count = len(text) // key_len
        column_order = self.get_column_order(key)
        matrix = [['' for _ in range(key_len)] for _ in range(row_count)]
        index = 0

        for column in column_order:
            for row in range(row_count):
                matrix[row][column] = text[index]
                index += 1

        decrypt_text = []

        for row in matrix:
            decrypt_text.extend(row)

        return ''.join(decrypt_text)
