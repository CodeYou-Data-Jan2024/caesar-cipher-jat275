# add your code here
def encrypt_caesar_cipher(plain_text, shift=5):
    encrypted_text = ""
    for char in plain_text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Find the position in 0-25, shift it, and take modulo 26 to wrap around
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's not an alphabetic character, don't change it
        else:
            encrypted_text += char
    return encrypted_text

# Ask the user for input
plain_text = input("Please enter a sentence: ")

# Encrypt the input
encrypted_text = encrypt_caesar_cipher(plain_text)

# Output the encrypted text
print("The encrypted sentence is:", encrypted_text)
