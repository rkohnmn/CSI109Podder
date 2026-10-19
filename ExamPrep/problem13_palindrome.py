# Palindrome checker
text = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase for uniform comparison
cleaned = text.replace(" ", "").lower()

# Check whether the text is a palindrome
if cleaned == cleaned[::-1]:
    print(f"'{text}' is a palindrome.")
else:
    print(f"'{text}' is not a palindrome.")
