#Program which asks user how many steps they walked today and prints based on if/elif/else

steps = int(input("Enter the number of steps you walked today: "))

if (steps < 5000):
    print("Keep moving!")
elif (steps >= 5000 and steps <= 8000):
    print("Almost there.")
else:
    print("Goal Met!")