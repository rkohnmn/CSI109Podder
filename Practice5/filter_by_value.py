# Filter a dictionary by value
marks = {"Alice": 90, "Bob": 65, "Charlie": 82, "Diana": 58}

# Pull out students with scores above 70
passed_students = {}
for student, score in marks.items():
    if score > 70:
        passed_students[student] = score

print("Scores above 70:", passed_students)
