text = input("Enter a string: ").lower()

# Count the vowels using a loop
count = 0
for char in text:
    if char in "aeiou":
        count = count + 1

print(f"Number of vowels: {count}")
