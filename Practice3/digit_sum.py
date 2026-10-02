number = int(input("Enter a number: "))

# Sum the digits using a loop
total = 0
temp = number
while temp > 0:
    total = total + temp % 10
    temp = temp // 10

print(f"Sum of digits of {number} = {total}")
