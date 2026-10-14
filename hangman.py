
import random
import os

with open("words.txt", "r") as file:
    inside = file.readlines()

word = random.choice(inside).strip()

if os.path.exists("stats.txt"):
    with open("stats.txt", "r") as stats:
        content = stats.read()
        content = content.splitlines()

    wins = int(content[0])
    losses = int(content[1])
else:
    wins = 0
    losses = 0

incorrect_guesses = 0

guessed = []

amount_of_guesses = 6

print("Guess a letter to find the word!")
print()

while incorrect_guesses < amount_of_guesses:

    print("the word is: ", end=" ")

    for letter in word:
        if letter in guessed:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print()
    print()

    if len(guessed) == 0:
        print("no guessed letters.")
    else:
        print("Guessed letters:", end=" ")
        for letter in guessed:
            print(letter, end=" ")
        print()

    print("amount of guesses you can get wrong:", amount_of_guesses - incorrect_guesses)

    if incorrect_guesses == 0:
        print("""
_________
|       |
|
|
|
|
|
|____________
""")

    elif incorrect_guesses == 1:
        print("""
_________
|       |
|       O
|
|
|
|
|____________
""")

    elif incorrect_guesses == 2:
        print("""
_________
|       |
|       O
|       |
|       |
|
|
|____________
""")

    elif incorrect_guesses == 3:
        print("""
_________
|       |
|       O
|      /|
|     / |
|
|
|____________
""")

    elif incorrect_guesses == 4:
        print("""
_________
|       |
|       O
|      /|\\
|     / | \\
|
|
|____________
""")

    elif incorrect_guesses == 5:
        print("""
_________
|       |
|       O
|      /|\\
|     / | \\
|      /
|     /
|____________
""")

    elif incorrect_guesses == 6:
        print("""
_________
|       |
|       O
|      /|\\
|     / | \\
|      / \\
|     /   \\
|____________
""")

    guess = input("Guess a letter: ")

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter a letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("Nice!", guess, "is in the word!")
    else:
        print("Sorry,", guess, "is not in the word.")
        incorrect_guesses = incorrect_guesses + 1

    finished = True

    for letter in word:
        if letter not in guessed:
            finished = False

    if finished:
        print()
        print("Congratulations! You guessed the word:", word)
        wins = wins + 1
        break

if incorrect_guesses == amount_of_guesses:
    print()
    print("Game over! You ran out of guesses.")
    print("The word was:", word)
    losses = losses + 1

with open("stats.txt", "w") as stats:
    stats.write(str(wins) + "\n")
    stats.write(str(losses) + "\n")

print()
print("Updated Stats - Wins:", wins, "Losses:", losses)