import random
password = input("Enter the password:")

def check_pass(password):
    trail= ""
    while trail != password:
        trail = str(random.randint(0,9999))
        print(trail)

        if trail == password:
            print("The password is:",password)
            
    return trail

print(check_pass(password))
print("Entered password is:",password)
