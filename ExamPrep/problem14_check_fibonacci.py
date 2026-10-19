# Check if a list is a Fibonacci series
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21]

# Verify if each element is the sum of the two preceding ones
is_fibonacci = True

if len(my_list) < 3:
    is_fibonacci = False
else:
    for i in range(2, len(my_list)):
        if my_list[i] != my_list[i - 1] + my_list[i - 2]:
            is_fibonacci = False
            break

print(is_fibonacci)
