"""
Author: Robert Thomas Kohn
Date: November 2, 2026
Description: Prompts the user for a block of text, cleans and normalizes it by removing
punctuation and converting to lowercase, counts word frequencies using a dictionary,
and displays the results sorted alphabetically.
Code of honesty: I have not copied from any source without proper citation.
"""

# 1. Prompt user for a block of text
print("Please enter a block of text:")
raw_text = input("> ")

# 2. Normalize text: convert to lowercase
text = raw_text.lower()

# 3. Remove punctuation characters using .replace()
punctuation = ".,!?:;\"'()-_"
for char in punctuation:
    text = text.replace(char, "")

# 4. Split cleaned text into individual words
words = text.split()

# 5. Count frequencies using a dictionary
word_counts = {}
for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# 6. Display sorted word counts
print("Word counts:")
for word in sorted(word_counts.keys()):
    print(f"{word}: {word_counts[word]}")

# 7. Print concluding thank-you message
print("Thank you for using the word count program!")
