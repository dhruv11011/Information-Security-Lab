def encrypt_rail_fence(text, keys):
    rail_matrix = [['\n' for _ in range(len(text))] for _ in range(keys)]
    direction = -1
    row, col = 0, 0
    for char in text:
        if row == 0 or row == keys - 1:
            direction *= -1
        rail_matrix[row][col] = char
        col += 1
        row += direction
    encrypted_text = ''.join(
        char for row in rail_matrix for char in row if char != '\n')
    return encrypted_text
def decrypt_rail_fence(text, keys):
    rail_matrix = [['\n' for _ in range(len(text))] for _ in range(keys)]
    direction = -1
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0 or row == keys - 1:
            direction *= -1
        rail_matrix[row][col] = '*'
        col += 1
        row += direction
    index = 0
    for row in range(keys):
        for col in range(len(text)):
            if rail_matrix[row][col] == '*' and index < len(text):
                rail_matrix[row][col] = text[index]
                index += 1
    direction = -1
    row, col = 0, 0
    decrypted_text = ''
    for i in range(len(text)):
        if row == 0 or row == keys - 1:
            direction *= -1
        if rail_matrix[row][col] != '\n':
            decrypted_text += rail_matrix[row][col]
        col += 1
        row += direction
    return decrypted_text
keys = 3
text = input("Enter Your Plain Text: ")
encrypted_text = encrypt_rail_fence(text, keys)
print("Cipher Text:", encrypted_text)
decrypted_text = decrypt_rail_fence(encrypted_text, keys)
print("Plain Text:", decrypted_text)