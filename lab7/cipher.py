import string
class Cipher:
    def __init__(self):
        self._alphabet = list(string.ascii_uppercase)
        self._reverse_alphabet = self._alphabet[::-1]

    def encrypt_message(self,message):
        message = message.upper()
        _encrypted_message = ""
        for char in message:
            if char in self._alphabet:
                _encrypted_message += self._encrypt_letter(char)
            else:
                _encrypted_message += char
        return _encrypted_message
    def decrypt_message(self,message):
        message = message.upper()
        _decrypted_message = ""
        for char in message:
            if char in self._alphabet:
                _decrypted_message += self._decrypt_letter(char)
            else:
                _decrypted_message += char
        return _decrypted_message
    def _encrypt_letter(self, letter):
        index = self._alphabet.index(letter)
        return self._reverse_alphabet[index]
    def _decrypt_letter(self,letter):
        index = self._reverse_alphabet.index(letter)
        return self._alphabet[index]