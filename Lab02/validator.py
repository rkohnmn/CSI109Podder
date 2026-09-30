"""
Author: Robert Thomas Kohn
Date: September 19, 2026
Description: A Reading Validator program that checks weather temperature readings for missing, unrealistic, or valid data.
Code of honesty: I have not copied from any source without proper citation.
"""

# Get temperature input from the user
raw_reading = input("Enter a temperature reading: ").strip()

# Classify the input using a single if/elif/else chain
# Check if the input is empty or "N/A"
if raw_reading == "" or raw_reading.upper() == "N/A":
    print("Missing value -- skipped.")

# Check if the numerical temperature reading is below -90 or above 60
elif float(raw_reading) < -90 or float(raw_reading) > 60:
    print(f"Implausible reading ({raw_reading}) -- flagged.")

# Any plausible, non-missing reading is accepted
else:
    print(f"Accepted: {raw_reading} C")
