# Multiplication table up to 10
n = int(input("Enter a number: "))

# Display multiplication table from 1 to 10
for i in range(1, 11):
    result = n * i
    print(f"{n} x {i} = {result}")
