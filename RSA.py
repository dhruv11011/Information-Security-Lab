import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    n = p * q
    phi = (p-1) * (q-1)
    e = 65535
    d = mod_inverse(e, phi)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    key, n = pk
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher

def decrypt(pk, ciphertext):
    key, n = pk
    decrypted_values = [pow(char, key, n) for char in ciphertext]
    print("Decrypted values:", decrypted_values)

    # Print Unicode code points of each decrypted value
    unicode_points = [ord(chr(val)) for val in decrypted_values]
    print("Unicode code points:", unicode_points)

    # Convert decrypted values to characters and handle edge cases
    decrypted_message = ''.join([chr(val) if val < 128 else str(val) for val in decrypted_values])

    print("Decrypted message:", decrypted_message)
    return decrypted_message


if __name__ == '__main__':
    while True:
        print("Select Option: ")
        print("1.Generate Key")
        print("2.Encrypt")
        print("3.Decrypt")
        print("4.Exit")
        choice=input("Enter Your Choise: ")

        if choice == '1':
            p = int(input("Enter a prime number (p): "))
            q = int(input("Enter another prime number (q): "))
            public, private = generate_keypair(p, q)
            print("Public key: ", public)
            print("Private key: ", private)

        elif choice == '2':
            message = input("Enter a message to encrypt: ")
            public = input("Enter a public key (e, n): ")
            keys = public.split(", ")
            public = (int(keys[0]), int(keys[1]))
            encrypted_message = encrypt(public, message)
            print("Encrypted message:", encrypted_message)

        elif choice == '3':
            cipher = input("Enter a message to decrypt (comma-separated integers): ")
            ciphertext = [int(x.strip()) for x in cipher.split(",")]
            private = input("Enter a private key (d, n): ")
            pkeys = private.split(", ")
            private = (int(pkeys[0]), int(pkeys[1]))
            decrypted_message = decrypt(private, ciphertext)

        else:
            break
