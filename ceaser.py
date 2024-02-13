def encrypt(plain,key):
    cipher=""
    for i in range(len(plain)):
        char=plain[i]
        if(char.isupper()):
            cipher+=chr(((ord(char)+key-65)%26)+65)
        elif(char.islower()):
            cipher+=chr(((ord(char)+key-97)%26)+97)
        else:
            cipher+=char
    return cipher 

def decrypt(cipher,key):
    plain=""
    for i in range(len(cipher)):
        char=cipher[i]
        if(char.isupper()):
            plain+=chr(((ord(char)-key-65)%26)+65)
        elif(char.islower()):
            plain+=chr(((ord(char)-key-97)%26)+97)
        else:
            plain+=char
    return plain 

while True:
    print("Select Option: ")
    print("1.Encrypt")
    print("2.Decrypt")
    print("3.Exit")
    choise=input("Enter Your Choise: ")

    if(choise=='1'):
        key = int(input('Enter Key : '))
        plain = input('Enter Message to Encrypt : ')
        encrypt(plain,key)
        print("Cipher Text:" + encrypt(plain,key))
    
    if(choise=='2'):
        key = int(input('Enter Key : '))
        cipher = input('Enter Message to Decrypt : ')
        decrypt(cipher,key)
        print("Plain Text:" + decrypt(cipher,key))
    
    if(choise=='3'):
        break
