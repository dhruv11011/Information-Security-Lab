import random
import math
def rsa_algorithm():
    # Step 1: Generate two large prime numbers, p and q
    p = generate_large_prime()
    q = generate_large_prime()
    # Step 2: Compute n = p * q
    n = p * q
    # Step 3: Compute the totient function, phi(n) = (p-1) * (q-1)
    phi_n = (p - 1) * (q - 1)
    # Step 4: Choose a public key 'e' such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = choose_public_key(phi_n)
    # Step 5: Compute the private key 'd' such that (d * e) mod phi(n) = 1
    d = mod_inverse(e, phi_n)
    # Display public and private keys
    print('Public Key:')
    print(f'n = {n}')
    print(f'e = {e}')
    print('Private Key:')
    print(f'n = {n}')
    print(f'd = {d}')
    # Step 6: Encryption
    message = input('Enter the message to encrypt: ')
    encrypted = encrypt(message, e, n)
    print(f'Encrypted Message: {encrypted}')
    # Step 7: Decryption
    decrypted = decrypt(encrypted, d, n)
    print(f'Decrypted Message: {decrypted}')
def generate_large_prime():
    # Function to generate a large prime number
    # (You may want to use a more sophisticated method for generating primes in a real application)
    p = random.randint(2**10, 2**12)
    while not isprime(p):
        p = random.randint(2**10, 2**12)
    return p
def isprime(num):
    # Function to check if a number is prime
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def choose_public_key(phi_n):
    # Function to choose a public key 'e'
    # For simplicity, we'll choose a small odd number
    e = 3
    while math.gcd(e, phi_n) != 1:
        e += 2
    return e
def mod_inverse(a, m):
    # Function to compute the modular inverse of 'a' mod 'm'
    _, d, _ = extended_gcd(a, m)
    return d % m
def extended_gcd(a, b):
    # Extended Euclidean Algorithm to find gcd(a, b) and coefficients x, y
    if b == 0:
        return a, 1, 0
    else:
        g, x, y = extended_gcd(b, a % b)
        return g, y, x - (a // b) * y
def encrypt(message, e, n):
    # Function to encrypt a message using RSA algorithm
    message_ascii = [ord(char) for char in message]
    cipher_text = [pow(char, e, n) for char in message_ascii]
    return cipher_text
def decrypt(encrypted_message, d, n):
    # Function to decrypt a message using RSA algorithm
    decrypted_ascii = [pow(char, d, n) for char in encrypted_message]
    decrypted_message = ''.join(chr(char) for char in decrypted_ascii)
    return decrypted_message

# Run the RSA algorithm
rsa_algorithm()
