"""
Author: Robert Thomas Kohn
Date: October 6, 2026
Description: A number guessing game where the player has 3 chances to guess
a secret number between 1 and 100.
Code of honesty: I have not copied from any source without proper citation.
"""

import random

# pick random number
secret_number = random.randint(1, 100)

# total chances and guesses
max_chances = 3
guess_count = 0
won = False

print("Guess the number (1-100). You have 3 chances.")

# loop for 3 guesses
while guess_count < max_chances:
    guess_count = guess_count + 1
    guess = int(input(f"Guess #{guess_count}: "))

    # check guess
    if guess == secret_number:
        print(f"Match! You got it in {guess_count} guesses.")
        won = True
        break
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")

# if lost
if not won:
    print(f"Out of chances! The secret number was {secret_number}.")
