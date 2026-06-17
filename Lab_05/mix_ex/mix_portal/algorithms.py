ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


class CaesarCipher:
    def encrypt_text(self, text: str, key: int) -> str:
        result = []
        for char in text.upper():
            if char in ALPHABET:
                index = ALPHABET.index(char)
                result.append(ALPHABET[(index + key) % len(ALPHABET)])
            else:
                result.append(char)
        return "".join(result)

    def decrypt_text(self, text: str, key: int) -> str:
        return self.encrypt_text(text, -key)


class VigenereCipher:
    def encrypt_text(self, text: str, key: str) -> str:
        return self._transform(text, key, encrypt=True)

    def decrypt_text(self, text: str, key: str) -> str:
        return self._transform(text, key, encrypt=False)

    def _transform(self, text: str, key: str, encrypt: bool) -> str:
        clean_key = "".join(char for char in key.upper() if char in ALPHABET)
        if not clean_key:
            return text.upper()

        result = []
        key_index = 0
        for char in text.upper():
            if char in ALPHABET:
                shift = ALPHABET.index(clean_key[key_index % len(clean_key)])
                if not encrypt:
                    shift = -shift
                index = ALPHABET.index(char)
                result.append(ALPHABET[(index + shift) % len(ALPHABET)])
                key_index += 1
            else:
                result.append(char)
        return "".join(result)


class PlayfairCipher:
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    def format_key(self, key: str):
        key = key.upper().replace("J", "I")
        formatted = []
        for letter in key:
            if letter.isalpha() and letter not in formatted:
                formatted.append(letter)
        for letter in self.alphabet:
            if letter not in formatted:
                formatted.append(letter)
        return formatted

    def create_matrix(self, key: str):
        formatted_key = self.format_key(key)
        return [formatted_key[index : index + 5] for index in range(0, 25, 5)]

    def find_position(self, matrix, letter: str):
        for row_index, row in enumerate(matrix):
            if letter in row:
                return row_index, row.index(letter)
        raise ValueError(f"Letter {letter} not found in matrix")

    def format_text(self, text: str):
        text = "".join(letter for letter in text.upper().replace("J", "I") if letter.isalpha())
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

    def encrypt_text(self, text: str, key: str):
        matrix = self.create_matrix(key)
        return "".join(self._encrypt_pair(matrix, pair) for pair in self.format_text(text))

    def decrypt_text(self, text: str, key: str):
        matrix = self.create_matrix(key)
        text = "".join(letter for letter in text.upper().replace("J", "I") if letter.isalpha())
        output = []
        for index in range(0, len(text), 2):
            pair = text[index : index + 2]
            if len(pair) == 2:
                output.append(self._decrypt_pair(matrix, pair))
        return "".join(output)

    def _encrypt_pair(self, matrix, pair: str):
        row1, col1 = self.find_position(matrix, pair[0])
        row2, col2 = self.find_position(matrix, pair[1])
        if row1 == row2:
            return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        if col1 == col2:
            return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        return matrix[row1][col2] + matrix[row2][col1]

    def _decrypt_pair(self, matrix, pair: str):
        row1, col1 = self.find_position(matrix, pair[0])
        row2, col2 = self.find_position(matrix, pair[1])
        if row1 == row2:
            return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        if col1 == col2:
            return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        return matrix[row1][col2] + matrix[row2][col1]


class RailFenceCipher:
    def encrypt_text(self, text: str, key: int):
        text = text.upper()
        if key <= 1 or key >= len(text):
            return text
        rails = ["" for _ in range(key)]
        row = 0
        direction = 1
        for letter in text:
            rails[row] += letter
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        return "".join(rails)

    def decrypt_text(self, text: str, key: int):
        text = text.upper()
        if key <= 1 or key >= len(text):
            return text
        pattern = []
        row = 0
        direction = 1
        for _ in text:
            pattern.append(row)
            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1
            row += direction
        rail_lengths = [pattern.count(index) for index in range(key)]
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(text[start : start + length]))
            start += length
        rail_indexes = [0] * key
        output = []
        for rail in pattern:
            output.append(rails[rail][rail_indexes[rail]])
            rail_indexes[rail] += 1
        return "".join(output)


class TranspositionCipher:
    def format_key(self, key: str):
        return "".join(letter for letter in key.upper() if letter.isalpha())

    def format_text(self, text: str):
        return "".join(letter for letter in text.upper() if letter.isalpha())

    def get_column_order(self, key: str):
        return [index for index, _ in sorted(enumerate(key), key=lambda item: (item[1], item[0]))]

    def create_matrix(self, text: str, key: str):
        key_len = len(key)
        rows = []
        for index in range(0, len(text), key_len):
            row = list(text[index : index + key_len])
            while len(row) < key_len:
                row.append("X")
            rows.append(row)
        return rows

    def encrypt_text(self, text: str, key: str):
        key = self.format_key(key)
        text = self.format_text(text)
        if not key:
            return text
        matrix = self.create_matrix(text, key)
        output = []
        for column in self.get_column_order(key):
            for row in matrix:
                output.append(row[column])
        return "".join(output)

    def decrypt_text(self, text: str, key: str):
        key = self.format_key(key)
        text = self.format_text(text)
        if not key:
            return text
        key_len = len(key)
        row_count = len(text) // key_len
        matrix = [["" for _ in range(key_len)] for _ in range(row_count)]
        index = 0
        for column in self.get_column_order(key):
            for row in range(row_count):
                matrix[row][column] = text[index]
                index += 1
        return "".join("".join(row) for row in matrix)


def run_classical_cipher(algorithm: str, action: str, text: str, key: str):
    algorithm = algorithm.lower()
    action = action.lower()
    if algorithm == "caesar":
        cipher = CaesarCipher()
        parsed_key = int(key)
    elif algorithm == "vigenere":
        cipher = VigenereCipher()
        parsed_key = key
    elif algorithm == "playfair":
        cipher = PlayfairCipher()
        parsed_key = key
    elif algorithm == "railfence":
        cipher = RailFenceCipher()
        parsed_key = int(key)
    elif algorithm == "transposition":
        cipher = TranspositionCipher()
        parsed_key = key
    else:
        raise ValueError("Unsupported classical algorithm")

    if action == "encrypt":
        return cipher.encrypt_text(text, parsed_key)
    if action == "decrypt":
        return cipher.decrypt_text(text, parsed_key)
    raise ValueError("Unsupported action")
