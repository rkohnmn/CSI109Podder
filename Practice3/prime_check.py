number = int(input("Enter a number (1-100): "))

# Validate the input range
if number < 1 or number > 100:
    print("Please enter a number between 1 and 100.")
else:
    # Check if the number is prime using a loop
    if number < 2:
        print(f"{number} is not prime.")
    else:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            print(f"{number} is prime.")
        else:
            print(f"{number} is not prime.")
