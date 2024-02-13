import string

def substitution_cipher(plaintext, substitution_key):
    # Define the alphabet
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    
    # Create a dictionary to map each letter to its substitution
    substitution_dict = dict(zip(alphabet, substitution_key))
    
    # Encrypt the plaintext
    encrypted_text = ''.join(substitution_dict.get(char, char) for char in plaintext)
    
    return encrypted_text

# Example usage:
plaintext_message = "Hello, World!"
substitution_key = "XyZAbCdEfGhIjKlMnOpQrStUvWxYz"
encrypted_message = substitution_cipher(plaintext_message, substitution_key)

print("Plaintext:", plaintext_message)
print("Substitution Key:", substitution_key)
print("Encrypted Text:", encrypted_message)
