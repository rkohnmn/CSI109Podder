# Triangle pattern of consecutive numbers
k = int(input("Enter number of rows: "))

# Print consecutive numbers forming a triangle
current_num = 1
for row in range(1, k + 1):
    for col in range(row):
        print(current_num, end="")
        current_num = current_num + 1
    print()
