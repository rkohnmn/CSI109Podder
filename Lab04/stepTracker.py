"""
Author: Robert Thomas Kohn
Date: October 19, 2026
Description: Logs daily steps, appends weekend data, slices weekdays and weekends, and filters days meeting an 8000-step goal.
Code of honesty: I have not copied from any source without proper citation.
"""

# Part 1: Step Tracker
# Step counts logged Monday to Saturday
steps = [6234, 8120, 4510, 10250, 7800, 12030]

# Write your code below this line

# 1. Initial logging summary: count of days, first day, and last day using negative index
print(f"Days logged so far: {len(steps)}")
print(f"Monday: {steps[0]}")
print(f"Saturday: {steps[-1]}")

# 2. Append Sunday count and show updated list
steps.append(3900)
print(f"Full week: {steps}")
print(f"Days logged now: {len(steps)}")

# 3. Slicing weekdays (first 5) and weekend (last 2)
weekdays = steps[:5]
weekend = steps[5:]
print(f"Weekdays: {weekdays}")
print(f"Weekend: {weekend}")

# 4. Weekly total and average formatted to one decimal place
total_steps = sum(steps)
average_per_day = total_steps / len(steps)
print(f"Total steps: {total_steps}")
print(f"Average per day: {average_per_day:.1f}")

# 5. Filter counts meeting the 8000-step goal using the append-in-a-loop pattern
goal_steps = []
for count in steps:
    if count >= 8000:
        goal_steps.append(count)

print(f"Days meeting the 8000-step goal: {goal_steps}")
print(f"That is {len(goal_steps)} out of {len(steps)} days.")
