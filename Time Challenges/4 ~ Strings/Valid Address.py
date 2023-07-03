email = input("Email: ")

isValid = True

if email.count("@") != 1: isValid = False
if email.count(".") < 1: isValid = False

print(isValid)