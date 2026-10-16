# Combine values for matching keys across dictionaries
data = [
    {"apple": 2, "banana": 3},
    {"banana": 1, "orange": 5},
    {"apple": 4}
]

combined = {}

# Add up counts for each matching item
for item in data:
    for fruit, count in item.items():
        if fruit in combined:
            combined[fruit] += count
        else:
            combined[fruit] = count

print("Combined counts:", combined)
