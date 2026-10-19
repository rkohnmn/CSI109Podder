# Sum of all integers from 1 to n
n = int(input("Enter an integer n: "))

# Calculate the sum using a loop
total = 0
for i in range(1, n + 1):
    total = total + i

# Display the result
print(f"The sum of integers from 1 to {n} is: {total}")
