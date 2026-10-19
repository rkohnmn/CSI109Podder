# Cookie recipe ingredient calculator
num_cookies = int(input("How many cookies do you want to make? "))

# Calculate ingredient quantities (proportional to 48 cookies)
factor = num_cookies / 48
sugar = 1.5 * factor
butter = 1.0 * factor
flour = 2.75 * factor

# Display ingredient quantities
print(f"Sugar: {sugar:.2f} cups")
print(f"Butter: {butter:.2f} cups")
print(f"Flour: {flour:.2f} cups")
