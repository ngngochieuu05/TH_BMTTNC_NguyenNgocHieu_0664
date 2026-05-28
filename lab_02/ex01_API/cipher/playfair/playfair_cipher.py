class PlayfairCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def format_key(self, key: str):
        key = key.upper().replace("J", "I")
        formatted_key = []

        for letter in key:
            if letter.isalpha() and letter not in formatted_key:
                formatted_key.append(letter)

        if not formatted_key:
            raise ValueError("Key must contain letters")

        for letter in self.alphabet:
            if letter not in formatted_key:
                formatted_key.append(letter)

        return formatted_key

    def normalize_text(self, text: str):
        return ''.join(letter for letter in text.upper().replace("J", "I") if letter.isalpha())

    def create_matrix(self, key: str):
        formatted_key = self.format_key(key)
        matrix = []

        for index in range(0, 25, 5):
            matrix.append(formatted_key[index:index + 5])

        return matrix

    def find_position(self, matrix, letter: str):
        for row_index, row in enumerate(matrix):
            if letter in row:
                return row_index, row.index(letter)

        return None, None

    def format_text(self, text: str):
        text = self.normalize_text(text)
        pairs = []
        index = 0

        while index < len(text):
            first_letter = text[index]

            if index + 1 < len(text):
                second_letter = text[index + 1]
                if first_letter == second_letter:
                    pairs.append(first_letter + "X")
                    index += 1
                else:
                    pairs.append(first_letter + second_letter)
                    index += 2
            else:
                pairs.append(first_letter + "X")
                index += 1

        return pairs

    def encrypt_pair(self, matrix, pair: str):
        row1, col1 = self.find_position(matrix, pair[0])
        row2, col2 = self.find_position(matrix, pair[1])

        if row1 == row2:
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]

        if col1 == col2:
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]

        return matrix[row1][col2] + matrix[row2][col1]

    def decrypt_pair(self, matrix, pair: str):
        row1, col1 = self.find_position(matrix, pair[0])
        row2, col2 = self.find_position(matrix, pair[1])

        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]

        if col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]

        return matrix[row1][col2] + matrix[row2][col1]

    def encrypt_text(self, text: str, key: str):
        matrix = self.create_matrix(key)
        pairs = self.format_text(text)
        encrypt_text = []

        for pair in pairs:
            encrypt_text.append(self.encrypt_pair(matrix, pair))

        return ''.join(encrypt_text)

    def decrypt_text(self, text: str, key: str):
        matrix = self.create_matrix(key)
        text = self.normalize_text(text)
        decrypt_text = []

        for index in range(0, len(text), 2):
            pair = text[index:index + 2]
            if len(pair) == 2:
                decrypt_text.append(self.decrypt_pair(matrix, pair))

        return self.remove_filler_x(''.join(decrypt_text))

    def remove_filler_x(self, text: str):
        cleaned_text = []

        for index, letter in enumerate(text):
            is_middle_filler = (
                letter == "X"
                and 0 < index < len(text) - 1
                and text[index - 1] == text[index + 1]
                and index % 2 == 1
            )
            is_padding_x = letter == "X" and index == len(text) - 1

            if not is_middle_filler and not is_padding_x:
                cleaned_text.append(letter)

        return ''.join(cleaned_text)
