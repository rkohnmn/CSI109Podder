# Find all prime numbers from 1 to 20 using a nested loop
for number in range(2, 21):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print(number, end=" ")

print()
