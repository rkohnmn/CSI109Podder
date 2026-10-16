# Count occurrences using a dictionary
words = ["cat", "dog", "cat", "bird", "dog", "cat"]
counts = {}

# Count how many times each word appears
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print("Word counts:", counts)
