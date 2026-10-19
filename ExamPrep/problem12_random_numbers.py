# Generate 20 random integers and display statistics
import random

numbers = []

# Generate 20 random integers between 1 and 100
for i in range(20):
    numbers.append(random.randint(1, 100))

# Calculate statistics
total = sum(numbers)
average = total / len(numbers)
smallest = min(numbers)
largest = max(numbers)

# Display results
print("All of the numbers in the list:", numbers)
print("The sum of the numbers in the list:", total)
print(f"The average of the numbers in the list: {average:.2f}")
print("The smallest number in the list:", smallest)
print("The largest number in the list:", largest)
