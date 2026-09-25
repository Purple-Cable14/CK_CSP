# CK, Password Strength Check

length = False

uppercase = False

lowercase = False

number = False

symbol = False

password = input("What is your password: ").strip()

for letter in password:
    if len(password) >= 8:
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

score = 0

if length:
    score += 1

if uppercase:
    score += 1

if lowercase:
    score += 1

if number:
    score += 1

if symbol:
    score += 1

if score == 5:
    strength = "Strong"
elif score >= 3:
    strength = "Medium"
else:
    strength = "Weak"

print(f"At least 8 characters: {length}")

print(f"Has an uppercase letter: {uppercase}")

print(f"Has a lowercase: {lowercase}")

print(f"Has a number: {number}")

print(f"Has a symbol: {symbol}")

print(f"Strength: {strength}")

if strength != "Strong":
    print("You are missing:")

    if length == False:
        print("At least 8 characters,")

    if uppercase == False:
        print("At least one uppercase letter,")

    if lowercase == False:
        print("At least one lowercase letter,")

    if number == False:
        print("At least one number")

    if symbol == False:
        print("At least one symbol")