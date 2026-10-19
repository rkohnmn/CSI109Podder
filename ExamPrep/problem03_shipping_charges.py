# Calculate shipping charges based on package weight
weight = float(input("Enter the weight of the package in pounds: "))

# Determine shipping charge per 500 miles
if weight <= 2:
    rate = 1.50
elif weight <= 6:
    rate = 3.00
elif weight <= 10:
    rate = 4.00
else:
    rate = 4.75

# Display shipping rate
print(f"Shipping charge: ${rate:.2f} per 500 miles")
