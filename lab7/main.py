# Naithen Ramirez, cris padilla 
# Oct 10, 2024 
# This program is a cipher program that allows the user to encrypt or decrypt a message.

from cipher import Cipher  
from caesar import CaesarCipher
from check_input import get_int_range

def main():
    """
    Main function to handle user input for encryption and decryption using Atbash or Caesar cipher.
    """
    while True:
        
        print("Secret Decoder Ring:")
        print("1. Encrypt")
        print("2. Decrypt")
        decoder = get_int_range("Enter 1 or 2: ", 1, 2)
        
        if decoder == 1:  # Encrypt
            print('1. Atbash')
            print('2. Caesar')
            encryption_type = get_int_range("Enter 1 or 2: ", 1, 2)
            message = input("Enter message: ")

            if encryption_type == 1:  # Atbash
                cipher = Cipher()
                encrypted_message = cipher.encrypt_message(message)
                shift = None  # No shift for Atbash

            elif encryption_type == 2:  # Caesar
                shift = get_int_range("Enter shift value: ", 1, 25)
                cipher = CaesarCipher(shift)
                encrypted_message = cipher.encrypt_message(message)

            try:  # Save encrypted message and shift value to file
                with open('message.txt', 'w') as file:
                    file.write(f"{shift}\n{encrypted_message}")
                print("Encrypted message saved to 'message.txt'.")
            except:
                print("Error saving encrypted message.")

        elif decoder == 2:  # Decrypt
            print('1. Atbash')
            print('2. Caesar')
            decryption_type = get_int_range("Enter 1 or 2: ", 1, 2)

            try:  # Read encrypted message and shift value from file
                with open('message.txt', 'r') as file:
                    saved_shift = file.readline().strip()
                    message = file.read().strip()
            except FileNotFoundError:
                print("No encrypted message found to decrypt.")
                continue

            if decryption_type == 1:  # Atbash
                if saved_shift != 'None':
                    print("Error: The saved message is not encrypted using Atbash.")
                    continue
                cipher = Cipher()
                decrypted_message = cipher.decrypt_message(message)
                print(f"Decrypted message: {decrypted_message}")

            elif decryption_type == 2:  # Caesar
                shift = get_int_range("Enter shift value: ", 1, 25)
                if saved_shift != str(shift):
                    print("Error: The shift value does not match the one used for encryption.")
                    continue
                cipher = CaesarCipher(shift)
                decrypted_message = cipher.decrypt_message(message)
                print(f"Decrypted message: {decrypted_message}")


if __name__ == "__main__":
    main()