"""
Author: Robert Thomas Kohn
Date: October 6, 2026
Description: Longest streak of increasing numbers.
Code of honesty: I have not copied from any source without proper citation.
"""

# variables
current_streak = 0
max_streak = 0
previous_number = None

# loop for input
while True:
    user_input = int(input("Enter a positive integer (-1 to stop): "))

    # stop on -1
    if user_input == -1:
        break

    # check if positive
    if user_input <= 0:
        print("Invalid input. Please enter a positive number.")
        continue

    # streak logic
    if previous_number is None:
        current_streak = 1
    else:
        if user_input > previous_number:
            current_streak = current_streak + 1
        else:
            current_streak = 1

    previous_number = user_input

    # update max streak
    if current_streak > max_streak:
        max_streak = current_streak

# print result
print(f"Longest increasing streak: {max_streak}")
