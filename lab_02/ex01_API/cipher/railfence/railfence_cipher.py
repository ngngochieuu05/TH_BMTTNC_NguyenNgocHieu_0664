class RailFenceCipher:
    def __init__(self):
        pass

    def encrypt_text(self, text: str, key: int):
        text = text.upper()

        if key <= 1 or key >= len(text):
            return text

        rails = ['' for _ in range(key)]
        row = 0
        direction = 1

        for letter in text:
            rails[row] += letter

            if row == 0:
                direction = 1
            elif row == key - 1:
                direction = -1

            row += direction

        return ''.join(rails)

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
            rails.append(list(text[start:start + length]))
            start += length

        rail_indexes = [0] * key
        decrypt_text = []

        for rail in pattern:
            decrypt_text.append(rails[rail][rail_indexes[rail]])
            rail_indexes[rail] += 1

        return ''.join(decrypt_text)
