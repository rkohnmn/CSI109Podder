a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

# Compare a and b and put the smaller number first
if a > b:
    temp = a
    a = b
    b = temp
# Compare c and d and put the smaller number first
if c > d:
    temp = c
    c = d
    d = temp
# Compare a and c and put the smaller number first
if a > c:
    temp = a
    a = c
    c = temp
# Compare b and d and put the smaller number first
if b > d:
    temp = b
    b = d
    d = temp
# Compare b and c and put the smaller number first
if b > c:
    temp = b
    b = c
    c = temp

# The numbers are now in order: a <= b <= c <= d
print("Largest:", d, "Second largest:", c, "Smallest:", a)