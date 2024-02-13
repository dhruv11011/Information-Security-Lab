def matrix_inverse(matrix, modulo):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det %= modulo
    det_inverse = None
    for i in range(1, modulo):
        if (det * i) % modulo == 1:
            det_inverse = i
            break
    if det_inverse is None:
        raise ValueError("Matrix is not invertible")
    
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    inverse = [[(d * det_inverse) % modulo, (-b * det_inverse) % modulo],
               [(-c * det_inverse) % modulo, (a * det_inverse) % modulo]]
    return inverse

def matrix_modulo(matrix, modulo):
    return [[element % modulo for element in row] for row in matrix]

def matrix_multiply(matrix1, matrix2, modulo):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)    
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrix dimensions are not suitable for multiplication")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                result[i][j] %= modulo

    return result

def get_key_matrix():
    key_matrix = []
    print("Enter 2x2 key matrix (each element separated by a space):")
    for _ in range(2):
        row = input().split()
        if len(row) != 2:
            print("Please enter exactly 2 elements per row.")
            return get_key_matrix()
        key_matrix.append([int(row[0]), int(row[1])])
    return key_matrix

def hill_cipher_encrypt(plaintext, key_matrix, modulo):
    n = len(key_matrix)
    padded_plain = plaintext + 'X' * (n - len(plaintext) % n)
    ciphertext = ''
    for i in range(0, len(padded_plain), n):
        block = [[ord(ch) - ord('A') for ch in padded_plain[i:i + n]]]
        encrypted_block = matrix_modulo(
            matrix_multiply(block, key_matrix, modulo), modulo)
        ciphertext += ''.join([chr(e + ord('A')) for e in encrypted_block[0]])
    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix, modulo):
    inverse_key = matrix_inverse(key_matrix, modulo)
    n = len(key_matrix)
    plaintext = ''
    for i in range(0, len(ciphertext), n):
        block = [[ord(ch) - ord('A') for ch in ciphertext[i:i + n]]]
        decrypted_block = matrix_modulo(
            matrix_multiply(block, inverse_key, modulo), modulo)
        plaintext += ''.join([chr(e + ord('A')) for e in decrypted_block[0]])
    return plaintext

while True:
    print("Select an option:")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        key_matrix = get_key_matrix()
        modulo = 26
        plaintext = input("Enter plaintext (in uppercase letters): ")
        ciphertext = hill_cipher_encrypt(plaintext, key_matrix, modulo)
        print("Ciphertext:", ciphertext)
    elif choice == '2':
        key_matrix = get_key_matrix()
        modulo = 26
        ciphertext = input("Enter ciphertext (in uppercase letters): ")
        decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix, modulo)
        print("Decrypted Text:", decrypted_text)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
