# Access and update a nested dictionary
students = {
    "Alice": {"age": 20, "major": "CS"},
    "Bob": {"age": 22, "major": "Math"}
}

# Print Bob's major
print("Bob's major:", students["Bob"]["major"])

# Add GPA for Alice
students["Alice"]["GPA"] = 3.8

# Print Alice's updated info and full dictionary
print("Alice's updated info:", students["Alice"])
print("Updated students:", students)
