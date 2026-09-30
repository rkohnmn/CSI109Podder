"""
Author: Robert Thomas Kohn
Date: September 12, 2026
Description: Asks three students for study hours, then reports the total, mean, and the mean as hours and minutes.
Code of honesty: I have not copied from any source without proper citation.
"""

# Get the hours.
hours_student1 = float(input("Hours for student 1: "))
hours_student2 = float(input("Hours for student 2: "))
hours_student3 = float(input("Hours for student 3: "))

# Total and mean.
total_hours = hours_student1 + hours_student2 + hours_student3
mean_hours = total_hours / 3

# Print the total and mean.
print(f"Total: {total_hours} hours")
print(f"Mean: {mean_hours:.1f} hours")

# Split the mean into hours and minutes with // and %.
whole_hours = mean_hours // 1         # whole hours
fraction_part = mean_hours % 1        # leftover fraction
leftover_minutes = fraction_part * 60 # fraction * 60 = minutes

# Print the hours and minutes.
print(f"That is {whole_hours:.0f} hours and {leftover_minutes:.0f} minutes.")
