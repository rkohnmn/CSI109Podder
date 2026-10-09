# Count even numbers in a list
numbers = [3, 6, 9, 12, 15, 18, 21]

# Loop through and count the evens
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1

print("Even numbers count:", count)
