# Check if a list is sorted
list1 = [1, 2, 3, 4, 5]
list2 = [1, 3, 2, 4, 5]

# See if it's in ascending order
def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True

print("List:", list1, "-> Sorted:", is_sorted(list1))
print("List:", list2, "-> Sorted:", is_sorted(list2))
