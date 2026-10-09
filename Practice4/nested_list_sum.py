# Sum all elements in a nested list
nested_list = [[1, 2], [3, 4], [5, 6]]

# Add up everything inside the sublists
total = 0
for sublist in nested_list:
    for num in sublist:
        total += num

print("Sum of all elements:", total)
