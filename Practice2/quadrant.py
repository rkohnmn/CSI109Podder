x = float(input("Enter x coordinate: "))
y = float(input("Enter y coordinate: "))

if x > 0:
    if y > 0:
        print("Quadrant I")
    elif y < 0:
        print("Quadrant IV")
    else:
        print("On the x-axis")

elif x < 0:
    if y > 0:
        print("Quadrant II")
    elif y < 0:
        print("Quadrant III")
    else:
        print("On the x-axis")

else:
    if y == 0:
        print("Origin")
    else:
        print("On the y-axis")