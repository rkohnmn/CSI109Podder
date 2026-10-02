number = int(input("Enter a number: "))

# Reverse the integer using a loop
reversed_num = 0
temp = number
while temp > 0:
    reversed_num = reversed_num * 10 + temp % 10
    temp = temp // 10

print(f"Reversed: {reversed_num}")
