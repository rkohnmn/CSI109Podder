"""
Author: Robert Thomas Kohn
Date: November 10, 2026
Description: Uses functions from stats_tools to clean and summarize temperature
data, displays a conversion table, and shows the difference between return and print.
Code of honesty: I have not copied from any source without proper citation.
"""

# 1. Start with imports from stats_tools
from stats_tools import mean, clean, summarize, celsius_to_fahrenheit, is_valid


# Part 2: Use Your Module

# 2. Begin with messy temperature list
messy = [24.5, 26.1, -999, 25.8, -999, 22.3, 250.0, 21.9]

# 3. Clean messy list, then filter out anything is_valid rejects
cleaned = clean(messy)

valid_readings = []
for reading in cleaned:
    if is_valid(reading):
        valid_readings.append(reading)

# 4. Print how many readings survived each stage
print(f"Started with {len(messy)} readings")
print(f"After removing -999: {len(cleaned)}")
print(f"After the plausibility check: {len(valid_readings)}")

# 5. Print summary from summarize() in a readable format
count, avg, min_temp, max_temp = summarize(valid_readings)
print(f"n={count} mean={avg:.2f} min={min_temp} max={max_temp}")

# 6. Print table of surviving readings in Celsius and Fahrenheit
print(f"{'C':>6} {'F':>6}")
for temp_c in valid_readings:
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c:>6.1f} {temp_f:>6.1f}")


# Part 3: Return vs Print

# 1. Define bad_mean and good_mean
def bad_mean(numbers):
    """Print the mean of a list of numbers instead of returning it."""
    print(sum(numbers) / len(numbers))


def good_mean(numbers):
    """Calculate and return the mean of a list of numbers."""
    return sum(numbers) / len(numbers)


# 2. Call each function on test readings, storing the result in a variable
test_readings = [72, 75, 68]
print()
print(f"Calling bad_mean({test_readings}) prints:")
bad_result = bad_mean(test_readings)
good_result = good_mean(test_readings)

# 3. Print what each variable actually contains
print(f"bad_mean returned {bad_result}")
print(f"good_mean returned {good_result:.2f}, and {good_result:.2f} * 2 = {good_result * 2:.2f}")

# 4 & 5. Try to use each result in a calculation (* 2) and catch the exception
try:
    bad_result * 2
except TypeError as e:
    print("Trying bad_mean's result * 2 raises:")
    print(f"TypeError: {e}")
