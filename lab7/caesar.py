from cipher import Cipher  

class CaesarCipher(Cipher):
    '''
    A cipher where each letter is shifted a certain number of places down the alphabet.
    '''
    def __init__(self):
        '''
        Initializes the CaesarCipher class with a default shift value of 3.
        '''
        super().__init__()
        self._shift = 3
        
    def encrypt_message(self,message):
        '''
        Encrypts the given message using the Caesar cipher.

        Parameters:
        message (str): The message to be encrypted.

        Returns:
        str: The encrypted message.
        '''
        message = message.upper()
        _encrypted_message = ""
        for char in message:
            if char in self._alphabet:
                _encrypted_message += self._encrypt_letter(char)
            else:
                _encrypted_message += char
        return _encrypted_message
    
    def decrypt_message(self,message):
        '''
        Decrypts the given message using the Caesar cipher.

        Parameters:
        message (str): The message to be decrypted.

        Returns:
        str: The decrypted message.
        '''
        message = message.upper()
        _decrypted_message = ""
        for char in message:
            if char in self._alphabet:
                _decrypted_message += self._decrypt_letter(char)
            else:
                _decrypted_message += char
        return _decrypted_message
    
    def _encrypt_letter(self, letter):
        '''
        Encrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be encrypted.

        Returns:
        str: The encrypted letter.
        '''
        index = self._alphabet.index(letter)
        return self._reverse_alphabet[(index + self._shift) % 26]
    
    def _decrypt_letter(self,letter):
        '''
        Decrypts a single letter using the Caesar cipher.

        Parameters:
        letter (str): The letter to be decrypted.

        Returns:
        str: The decrypted letter.
        '''
        index = self._reverse_alphabet.index(letter)
        return self._alphabet[(index + self._shift) % 26]