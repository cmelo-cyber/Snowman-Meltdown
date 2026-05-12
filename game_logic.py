#from snowman import WORDS
import random
from ascii import STAGES
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(secret_word, guessed_letters,mistakes= 0):
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    #print("Secret word selected: " + secret_word)  # for testing, later remove this line

    # TODO: Build your game loop here.
    # For now, simply prompt the user once:
    mistakes = 0
    guessed_letters = []
    max_try = 3   #len(secret_word) is not working there are only three stages for the snowman,
                # otherwise it is list index out of range
    correct_guess = 0
    found = False
    alphabet = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z"
    ]

    while mistakes < max_try and found is False:
        display_game_state( secret_word, guessed_letters, mistakes)
        guess = input("Guess a letter: ").lower()

        if guess not in alphabet:
            print("You need to enter a letter from the alphabet")
            continue
        elif guess in guessed_letters:
            print("Try another letter")
            continue

        print("----------------------------")
        print("You guessed:", guess, "\n")



        if guess not in secret_word: # it is a wrong guess a mistake
            mistakes += 1
        else: #it's a correct guess
            guessed_letters.append(guess)
            correct_guess += 1

        # Checking the ending criteria, winner or looser
        if correct_guess == len(secret_word):
            found = True
            print("Congratulation you win!!!")
        elif mistakes == max_try:    #len(secret_word)
            print("Sorry, you lose")