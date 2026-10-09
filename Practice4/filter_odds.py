# Filter odd numbers from a list
numbers = [3, 6, 9, 12, 15, 18, 21]

# Pull out just the odd numbers
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)

print("Odd numbers:", odd_numbers)
