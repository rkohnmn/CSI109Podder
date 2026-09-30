h1 = int(input("Enter first hour: "))
m1 = int(input("Enter first minute: "))

h2 = int(input("Enter second hour: "))
m2 = int(input("Enter second minute: "))

# Validate both times
if h1 < 0 or h1 > 23 or m1 < 0 or m1 > 59:
    print("Invalid time")
elif h2 < 0 or h2 > 23 or m2 < 0 or m2 > 59:
    print("Invalid time")
else:
    # Convert both times to total minutes
    time1 = h1 * 60 + m1
    time2 = h2 * 60 + m2

    # Find absolute difference
    difference = time1 - time2

    if difference < 0:
        difference = -difference

    # Convert difference back to hours and minutes
    hours = difference // 60
    minutes = difference % 60

    print(hours, "hours", minutes, "minutes")