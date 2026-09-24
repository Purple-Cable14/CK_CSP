# CK, Password Strength Check

length = False

uppercase = False

lowercase = False

number = False

symbol = False

password = input("What is your password: ").strip()

for letter in password:
    if (len(password)) >= 8:
        length = True

for letter in password:
    if letter.isupper():
        uppercase = True
        
for letter in password:
    if letter.islower():
        lowercase = True

for letter in password:
    if letter.isnumeric():
        number = True

for letter in password:
    if letter in "!@#$%^&*-_<>?":
        symbol = True

print(f"At least 8 characters: {length}")

print(f"Has an uppercase letter: {uppercase}")

print(f"Has a lowercase: {lowercase}")

print(f"Has a number: {number}")

print(f"Has a symbol: {symbol}")

score = 0
if (len(password)) >= 8:
