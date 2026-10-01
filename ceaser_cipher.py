# CK, Caeser Cipher

change = input("Would you like to (E)ncrypt or (D)ecrypt a message? ")

message = input("Enter your message: ")

shift_amount = input("Enter a shift amount: ")

for letter in message:
    if letter.isalpha():
        letter = ord(letter)
        letter += shift_amount
        print(letter)

