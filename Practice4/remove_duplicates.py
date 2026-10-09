# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 4, 5]

print("Original list:", numbers)

# Only keep items we haven't seen yet
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)

print("Without duplicates:", unique)
