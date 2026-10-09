# Rotate a list by k positions
numbers = [1, 2, 3, 4, 5]
k = 2

print("Original list:", numbers)

# Shift the list to the right by k spots
rotated = numbers[-k:] + numbers[:-k]

print("Rotated by", k, "positions:", rotated)
