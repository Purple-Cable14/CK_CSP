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