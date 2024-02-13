def columnar_transposition_encrypt(key, plaintext):
    num_cols = len(key)
    num_rows = (len(plaintext) + num_cols - 1) // num_cols
    matrix = [[''] * num_cols for _ in range(num_rows)]
    i = 0
    for row in range(num_rows):
        for col in range(num_cols):
            if i < len(plaintext):
                matrix[row][col] = plaintext[i]
                i += 1
    ciphertext = ''.join(matrix[row][col] for row in range(num_rows) for col in range(num_cols))
    return ciphertext

def columnar_transposition_decrypt(key, ciphertext):
    num_cols = len(key)
    num_rows = (len(ciphertext) + num_cols - 1) // num_cols
    col_order = [int(k) for k in key]
    
    matrix = [[''] * num_cols for _ in range(num_rows)]
    i = 0
    
    for col in range(num_cols):
        order = col_order.index(col + 1)
        for row in range(num_rows):
            if i < len(ciphertext):
                matrix[row][order] = ciphertext[i]
                i += 1
    
    plaintext = ''.join(matrix[row][col] for row in range(num_rows) for col in range(num_cols))
    return plaintext

# key = "43521"
# plaintext = "Dhruv Bhatt's Alias is Blackeyes"
key = input("Enter The Key In Number: ")

plaintext = input("Enter Your Plaintext: ")

encrypted_text = columnar_transposition_encrypt(key, plaintext)
decrypted_text = columnar_transposition_decrypt(key, encrypted_text)
print("Encrypted:", decrypted_text)
print("Decrypted:", encrypted_text)