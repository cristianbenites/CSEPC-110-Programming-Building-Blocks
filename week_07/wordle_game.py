"""
Title: Wordow Game
Author: Cristian Benites

Description:
    Wordow is a game in which the player has to guess the correct word.
    In addition to the built-in list, a player can import their own word list using the --file argument followed by the filepath.

"""

from random import choice
from sys import argv

# Reads the --file argument and sets the filepath
filepath = ""
for i in range(len(argv)):
    if argv[i] == "--file":
        filepath = argv[i + 1]

# Defaults
welcome_message = "Welcome the the Wordow, in this game you will guess a secret word following the guidelines:\n" \
    " - An underscore _ indicates that the letter was not present in the secret word\n" \
    " - A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.\n" \
    " - An uppercase letter indicates that the letter was present at that exact spot in the secret word. " \
    "(In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)\n"\
    " - If you enter a word longer than the hint, the remaining letters will be ignored.\n"\
    " - If you reach the maximum number of guesses, you lose the game.\n\n"\
    "You can also import your own wordlist using the \"--file\" argument followed by the file path. The file must have only one word per line.\n"

word_list = [
    "apple",
    "basket",
    "beach",
    "castle",
    "eagle",
    "guest",
    "gospel",
    "meaple",
    "moroni",
    "nelson",
    "savior",
    "school",
    "share",
    "strength",
    "travel",
    "yellow",
]
correct_answer = False
number_of_guesses = 0
MAX_NUMBER_OF_ATTEMPTS = 10

# If there is a filepath, we set the word list from the entered file
if (filepath):
    with open(filepath) as f:
        word_list = f.readlines()


# Now the game is prepared by choosing a word from the word list
# and defining the first hint
secret_word = choice(word_list).strip()
hint = "_" * len(secret_word)

def get_hint(guess):
    new_hint = ""
    for index in range(len(guess)):
        letter = guess[index]

        # Adds the letter when it is present in the secret word
        # or leave an underscore if it's not
        if (letter in secret_word):
            new_hint += letter
        else:
            new_hint += "_"

        # If the letter is already in the right place, make it uppercase
        if (letter == secret_word[index]):
            # This solution bellow seems faster than converting the string to a list,
            # changing the letter and transforming it back to string again.
            new_hint = new_hint[:index-1] + letter.upper() + new_hint[index+1:]

    return new_hint

print(welcome_message)
while(not correct_answer):
    if (number_of_guesses >= MAX_NUMBER_OF_ATTEMPTS):
        print("Sorry, you've reached the maximum number of attempts :(\n"
            f"The secret word was: {secret_word}")
        break

    # We format the hint to make it better to read by adding spaces between the characters
    formatted_hint = hint.replace("", " ")[1: -1]
    print(f"Remaining attempts: {MAX_NUMBER_OF_ATTEMPTS - number_of_guesses}")
    print(f"Your hint is: {formatted_hint}\n")

    # Get user's guess and process appropriately (adds characters for short words, removes characters for longer words)
    guess = input("What is your guess? ").lower()
    guess = guess[ 0 : len(secret_word)] if len(guess) >= len(secret_word) else guess + ("_" * (len(secret_word) - len(guess)))

    hint = get_hint(guess)
    number_of_guesses += 1

    if (hint == secret_word.upper()):
        correct_answer = True
        print("Congratulations! You guessed it!\n")
        print(f"It took {number_of_guesses} guess{'es' if number_of_guesses > 1 else ''}")
