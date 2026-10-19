# Display the first n prime numbers
n = int(input("Enter how many prime numbers to display: "))

count = 0
number = 2

# Find and print prime numbers until count reaches n
while count < n:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")
        count = count + 1

    number = number + 1

print()
