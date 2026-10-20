"""
Author: Robert Thomas Kohn
Date: October 19, 2026
Description: Parses a comma-separated string of daily temperature readings into floats and finds the min, max, average, and critical days.
Code of honesty: I have not copied from any source without proper citation.
"""

# Part 1: Analysis of Time-Series Data
# 15 consecutive daily temperature readings, in degrees Celsius
temp_data_string = "-14.5,-15.8,-12.3,-10.0,-13.7,-16.1,-15.4,-14.9,-13.2,-11.8,-10.5,-12.6,-14.1,-15.9,-16.2"

# Write your code below this line

# 1. Parse string into list of strings, then convert to list of floats
raw_strings = temp_data_string.split(",")
temps = []
for item in raw_strings:
    temps.append(float(item))

print(f"Readings: {len(temps)} days")

# 2 & 3. Find lowest and highest temperatures and their day numbers (index + 1)
# Start tracking from the first reading since all values are negative
lowest_temp = temps[0]
lowest_day = 1
highest_temp = temps[0]
highest_day = 1

for i in range(len(temps)):
    if temps[i] < lowest_temp:
        lowest_temp = temps[i]
        lowest_day = i + 1
    if temps[i] > highest_temp:
        highest_temp = temps[i]
        highest_day = i + 1

# Calculate average temperature to two decimal places
average_temp = sum(temps) / len(temps)

print(f"Lowest: {lowest_temp} C on day {lowest_day}")
print(f"Highest: {highest_temp} C on day {highest_day}")
print(f"Average: {average_temp:.2f} C")

# 4. Count critical events where temperature is strictly below -15.0 C
critical_days = 0
for temp in temps:
    if temp < -15.0:
        critical_days += 1

print(f"Critical days (below -15.0 C): {critical_days}")
