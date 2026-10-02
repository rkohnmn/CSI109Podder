x = int(input("Enter a number: "))

# Calculate and print factorials from 0! to x!
factorial = 1
print(f"0! = {factorial}")

for i in range(1, x + 1):
    factorial = factorial * i
    print(f"{i}! = {factorial}")
