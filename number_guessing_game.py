# CK, Number Guessing Game
import random

number = random.randint(1,101)

number_of_guesses = 1

print("I'm thinking of a number between 1 and 100. You have 6 tries to guess it! ")

while True:
    guesses = int(input(f"Guess number {number_of_guesses}: "))
    if guesses == number:
        print("You Win!")
        break
    elif number_of_guesses == 6:
        print(f"You Lose! The number was {number}!")
        break
    elif guesses > number:
        print("The number is lower.")
        number_of_guesses += 1
    else:
        print ("The number is higher.")
        number_of_guesses += 1

        direction = input("Do you want to (E)ncode or (D)ecode: ")
message = input("What is your message: ")
amount = int(input("How much do you want to shift: "))

def caeser_shift(message, shift):
    new_message = ""

    for letter in message:
        if letter.isalpha():
            number = ord(letter)
            number = number + shift

            if letter.isupper():
                if number > 90:
                    number = number - 26
                if number < 65:
                    number = number + 26
            else:
                if number > 122:
                    number = number - 26
                if number < 97:
                    number = number + 26

            letter = chr(number)

        new_message = new_message + letter

    return new_message

if direction == "E":
    message = caeser_shift(message, amount)
    print("Your encrypted message is:", message)
else:
    message = caeser_shift(message, -amount)
    print("Your decrypted message is:", message)
