age = int(input("Enter your age: "))

if age <= 17:
    if age <= 12:
        price = 5
    else:
        price = 8
else:
    if age <= 63:
        price = 12
    elif age >= 65:
        price = 7
    else:
        price = 0

print("Ticket price: $" + str(price))