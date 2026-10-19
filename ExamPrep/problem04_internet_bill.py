# Internet subscription monthly bill calculator
package = input("Enter the subscription package (A, B, or C): ")
hours = int(input("Enter the number of hours used: "))

# Calculate monthly bill
package = package.strip().upper()

if package == "A":
    bill = 9.95
    if hours > 10:
        bill = bill + (hours - 10) * 2.00
    print(f"Total monthly bill: ${bill:.2f}")
elif package == "B":
    bill = 13.95
    if hours > 20:
        bill = bill + (hours - 20) * 1.00
    print(f"Total monthly bill: ${bill:.2f}")
elif package == "C":
    bill = 19.95
    print(f"Total monthly bill: ${bill:.2f}")
else:
    print("Invalid subscription package.")
