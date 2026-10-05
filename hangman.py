# CK, Hangman
import random
print(random.choice(list))
# Create a list of 10 words on a seperate txt file (word,word,word)

# Create another file that holds win/loss counts

# Read your files
with open("words.txt","r") as file:
    words = file.read().split(",")
    content = file.read()
# Use split(",") on the content of the words txt document to create your list of words

# Pull win and lose totals from the other txt file and save them as 2 seperate variables

# Build the hangman game

#Save the correct word as a variable (random.choice(name of the list))
# Number of guesses
# What letters have been guessed

# Function to display the hangman (Needs number of wrong guesses)
"""_____
   |   |
   |   O
   |  /|\\
   |  / \\
   |_______
"""

# Function to show the letters and spaces (The correct word, letters that have been guessed)
# Variable for display word (starts as an empty string)
# Loop over the correct word
# Check if letter has been guessed
    # Then add the letter to the display word
# if they haven't guessed the letter
    #add an underscore to the display word
# return the finished display word (outside of the loop)

    # Main game loop (While true)
        #call function to show hangman
        # print function call to show display word
        # create variable and ask user to guess a letter
        # add the letter to list of guessed letters
        # check (if not letter in word:)
            # increase incorrect guesses
        # check if (display word) is same as the word
            # tell user they won
            # increase win total
            # ask if they want to play again
                #reset random word, rest wrong guess count
        # check to see if they lost (if they have 6 wrong guesses)
            # tell them they lost
            # tell them what the word was
            # increase the lost count
            # ask if they want to play again