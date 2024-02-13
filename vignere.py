def generate_key(message, key):
    key_length = len(key)
    key = list(key)
    if len(message) == key_length:
        return key
    else:
        for i in range(len(message) - key_length):
            key.append(key[i % key_length])
    return ''.join(key)

def encrypt(message, key):
    encrypted_text = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            char_offset = ord(char.upper()) - 65
            key_char = key[i]
            key_offset = ord(key_char.upper()) - 65
            encrypted_char = chr(((char_offset + key_offset) % 26) + 65)
            if char.islower():
                encrypted_char = encrypted_char.lower()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_message, key):
    decrypted_text = ''
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        if char.isalpha():
            char_offset = ord(char.upper()) - 65
            key_char = key[i]
            key_offset = ord(key_char.upper()) - 65
            decrypted_char = chr(((char_offset - key_offset) % 26) + 65)
            if char.islower():
                decrypted_char = decrypted_char.lower()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

if __name__ == "__main__":
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            keyword = input("Enter the key: ").upper()
            plaintext = input("Enter the plaintext: ").upper()
            key = generate_key(plaintext, keyword)
            ciphertext = encrypt(plaintext, key)
            print("Cipher Text: " + ciphertext)

        elif choice == "2":
            keyword = input("Enter the key: ").upper()
            ciphertext = input("Enter the ciphertext: ").upper()
            key = generate_key(ciphertext, keyword)
            decrypted_text = decrypt(ciphertext, key)
            print("Plain Text: " + decrypted_text)

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
