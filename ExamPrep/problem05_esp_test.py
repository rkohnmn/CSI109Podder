# ESP (extrasensory perception) testing program
import random

colors = ["Red", "Green", "Blue", "Orange", "Yellow"]

correct_guesses = 0

# Run the test 10 times
for i in range(1, 11):
    random_index = random.randint(0, len(colors) - 1)
    selected_color = colors[random_index]

    guess = input(f"Test #{i} - Enter your color guess: ").strip()
    print(f"The computer selected: {selected_color}")

    if guess.lower() == selected_color.lower():
        correct_guesses = correct_guesses + 1

# Display results
print(f"Number of correct guesses: {correct_guesses} out of 10")
