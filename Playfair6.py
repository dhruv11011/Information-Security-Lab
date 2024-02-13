def makeMatrix(key):
    key = key.replace(" ", "").upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    matrix = [['' for _ in range(6)] for _ in range(6)]
    key_index = 0
    for i in range(6):
        for j in range(6):
            if key_index < len(key):
                matrix[i][j] = key[key_index]
                key_index += 1
            else:
                for char in alphabet:
                    if char not in key and char not in matrix:
                        matrix[i][j] = char
                        break
    return matrix

def divideText(text):
    text = text.replace(" ", "").upper()
    divided_text = []
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            divided_text.append(text[i] + 'X')
            i += 1
        else:
            divided_text.append(text[i])
        i += 1
    if len(divided_text) % 2 != 0:
        divided_text.append('X')
    return [divided_text[i:i+2] for i in range(0, len(divided_text), 2)]

def findCharInMatrix(char, matrix):
    for i in range(6):
        for j in range(6):
            if matrix[i][j] == char:
                return i, j

def encrypt(plain_text, key_matrix):
    divided_text = divideText(plain_text)
    encrypted_text = ""
    for pair in divided_text:
        row1, col1 = findCharInMatrix(pair[0], key_matrix)
        row2, col2 = findCharInMatrix(pair[1], key_matrix)
        if row1 == row2:
            encrypted_text += key_matrix[row1][(col1 + 1) % 6]
            encrypted_text += key_matrix[row2][(col2 + 1) % 6]
        elif col1 == col2:
            encrypted_text += key_matrix[(row1 + 1) % 6][col1]
            encrypted_text += key_matrix[(row2 + 1) % 6][col2]
        else:
            encrypted_text += key_matrix[row1][col2]
            encrypted_text += key_matrix[row2][col1]
    return encrypted_text

def decrypt(encrypted_text, key_matrix):
    divided_text = divideText(encrypted_text)
    decrypted_text = ""
    for pair in divided_text:
        row1, col1 = findCharInMatrix(pair[0], key_matrix)
        row2, col2 = findCharInMatrix(pair[1], key_matrix)
        if row1 == row2:
            decrypted_text += key_matrix[row1][(col1 - 1) % 6]
            decrypted_text += key_matrix[row2][(col2 - 1) % 6]
        elif col1 == col2:
            decrypted_text += key_matrix[(row1 - 1) % 6][col1]
            decrypted_text += key_matrix[(row2 - 1) % 6][col2]
        else:
            decrypted_text += key_matrix[row1][col2]
            decrypted_text += key_matrix[row2][col1]
    return decrypted_text

if __name__ == "__main__":
    while True:
        key = input("Enter the key: ")
        key_matrix = makeMatrix(key)
        operation = input("1-> Encryption\n2-> Decryption\nChoose operation: ")
    
        if operation == "1":
            plaintext = input("Enter the text to be encrypted: ")
            encrypted_text = encrypt(plaintext, key_matrix)
            print("Encrypted text:", encrypted_text)
        elif operation == "2":
            encrypted_text = input("Enter the text to be decrypted: ")
            decrypted_text = decrypt(encrypted_text, key_matrix)
            print("Decrypted text:", decrypted_text)
        else:
            print("Invalid choice. Please select 1 for encryption or 2 for decryption.")
