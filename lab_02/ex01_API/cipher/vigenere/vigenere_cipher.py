from .alphabet import ALPHABET

class VigenereCipher:
    def __init__(self):
        self.alphabet = ALPHABET
    
    def encrypt_text(self, text: str, key: str):
        alphabet_len = len(self.alphabet)
        text = text.upper()
        key = key.upper()
        encrypt_text = []
        key_index = 0

        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                key_letter = key[key_index % len(key)]
                shift = self.alphabet.index(key_letter)
                output_index = (letter_index + shift) % alphabet_len
                output_letter = self.alphabet[output_index]
                encrypt_text.append(output_letter)
                key_index += 1
            else:
                encrypt_text.append(letter)

        return ''.join(encrypt_text)

    def decrypt_text(self, text: str, key: str):
        alphabet_len = len(self.alphabet)
        text = text.upper()
        key = key.upper()
        decrypt_text = []
        key_index = 0

        for letter in text:
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                key_letter = key[key_index % len(key)]
                shift = self.alphabet.index(key_letter)
                output_index = (letter_index - shift) % alphabet_len
                output_letter = self.alphabet[output_index]
                decrypt_text.append(output_letter)
                key_index += 1
            else:
                decrypt_text.append(letter)

        return ''.join(decrypt_text)
