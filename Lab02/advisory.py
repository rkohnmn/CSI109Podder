"""
Author: Robert Thomas Kohn
Date: September 19, 2026
Description: A Weather Advisory program that uses temperature and wind speed to determine the weather category and give the correct advisory using Boolean logic.
Code of honesty: I have not copied from any source without proper citation.
"""

# Get temperature and wind speed inputs
temperature = float(input("Temperature (C): "))
wind_speed = float(input("Wind speed (km/h): "))

# Classify the temperature into exactly one band
if temperature < 0:
    print("Freezing")
elif temperature < 15:
    print("Cold")
elif temperature < 25:
    print("Mild")
else:
    print("Warm")

# Determine and print the weather advisory using and/or operators
if temperature < 0 or wind_speed > 20:
    print("Hazardous conditions.")
elif (temperature >= 15 and temperature <= 25) and wind_speed < 10:
    print("Ideal conditions for field work.")
else:
    print("Conditions nominal.")
