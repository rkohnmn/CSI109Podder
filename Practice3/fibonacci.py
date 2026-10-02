n = int(input("How many Fibonacci numbers (1-50): "))

# Validate the input range
if n < 1 or n > 50:
    print("Please enter a number between 1 and 50.")
else:
    # Generate the Fibonacci series using a loop
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        temp = a + b
        a = b
        b = temp
    print()
