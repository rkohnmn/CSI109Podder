email = input("Enter your email: ").strip().lower()

if "@" not in email:
    print("That is not an email address")
elif "muhlenberg.edu" in email:
    print("Welcome Mule")
else:
    print("Please use your Muhlenberg email")