import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def createDigitalSignature(M, p, q):
    n = p * q
    phin = (p - 1) * (q - 1)

    # Find e (public key)
    e = 2
    while gcd(phin, e) != 1:
        e += 1

    # Calculate d (private key)
    d = modinv(e, phin)

    # Calculate digital signature
    S = pow(M, d, n)

    print('Message: ', M)
    print('p: ', p)
    print('q: ', q)
    print('d: ', d)
    print('S: ', S)

    return M, S, e, n

def verifyDigitalSignature(M, S, e, n):
    M1 = pow(S, e, n)

    print('Message: ', M)
    print('p: ', p)
    print('q: ', q)
    print('d: ', d)
    print('S: ', S)
    print('M1: ', M1)

    if M == M1:
        print('Digital Signature is verified')
    else:
        print('Digital Signature not verified')

# Get user input for the message
message = int(input("Enter the message (an integer): "))

# Example usage
p = 11
q = 7

M, S, e, n = createDigitalSignature(message, p, q)
verifyDigitalSignature(M, S, e, n)
