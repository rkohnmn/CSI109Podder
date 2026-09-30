side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if side1 == side2:
    if side2 == side3:
        print("Equilateral")
    else:
        print("Isosceles")
else:
    if side1 == side3:
        print("Isosceles")
    elif side2 == side3:
        print("Isosceles")
    else:
        print("Scalene")
