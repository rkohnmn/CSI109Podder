seconds=float(input("Enter the number of seconds: "))
hours=seconds//3600
minutes=(seconds%3600)//60
seconds=seconds%60
print("The time is: {} hours, {} minutes, and {} seconds.".format(int(hours), int(minutes), int(seconds)))