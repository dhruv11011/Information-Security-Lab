password = input("Enter the password: ")
output = ""
count = 0
for character in password:
    for a in range(97, 123):
        if character == chr(a):
            output += character
            break
        if character == chr(a - 22):
            output += character
            break
        if character == " ":
            output += character
            break
        count += 1
print("number of trials:",count)
print("The password is:"+output)


