x = int(input("What is temp in C: "))

if x < 0:
    print("It is very cold")
elif x < 15:
    print("It is cold")
elif x <= 25:
    print("It is warm")
else:
    print("It is very hot")
