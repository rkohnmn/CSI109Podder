# Store 20 numbers in a list and display statistics
numbers = []

# Ask the user for 20 numbers
for i in range(1, 21):
    val = float(input(f"Enter number {i} of 20: "))
    numbers.append(val)

# Calculate statistics
lowest = min(numbers)
highest = max(numbers)
total = sum(numbers)
average = total / len(numbers)

# Display results
print("All of the numbers in the list:", numbers)
print("The lowest number in the list:", lowest)
print("The highest number in the list:", highest)
print("The total of the numbers in the list:", total)
print(f"The average of the numbers in the list: {average:.2f}")
