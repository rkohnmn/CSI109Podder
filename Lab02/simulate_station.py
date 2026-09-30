"""
Author: Robert Thomas Kohn
Date: September 19, 2026
Description: A Simulated Station program that creates random weather data, classifies temperatures, checks field work advisories, and verifies that the data is realistic.
Code of honesty: I have not copied from any source without proper citation.
"""

import random
random.seed(67)
# ==============================================================================
# EXPLANATION OF RANDOM SEED:
# Computers cannot make truly random numbers on their own. They have to use these algorithms that are called pseudo random number generators. The seed works as the starting value for the whole process. Python takes the system time by default so the numbers come out different each run.
# Setting a seed with that random seed function makes the sequence stay the same every time. This helps when testing or when you need to repeat a simulation for class or research. For normal cases it seems better to skip it so fresh values appear.
# ==============================================================================

# Generate simulated sensor readings using random.randint()
simulated_temperature = random.randint(-10, 40)
simulated_wind_speed = random.randint(0, 40)

# Display the simulated reading header and values
print("Simulated reading")
print(f"Temperature: {float(simulated_temperature)} C")
print(f"Wind speed: {simulated_wind_speed} km/h")

# Determine the temperature band 
if simulated_temperature < 0:
    print("Freezing")
elif simulated_temperature < 15:
    print("Cold")
elif simulated_temperature < 25:
    print("Mild")
else:
    print("Warm")

# Determine the weather advisory 
if simulated_temperature < 0 or simulated_wind_speed > 20:
    print("Hazardous conditions.")
elif (simulated_temperature >= 15 and simulated_temperature <= 25) and simulated_wind_speed < 10:
    print("Ideal conditions for field work.")
else:
    print("Conditions nominal.")

# Validate the simulated reading 
if simulated_temperature < -90 or simulated_temperature > 60:
    print("Validator: flagged")
else:
    print("Validator: accepted")

# ==============================================================================
# PART 4:
# In real programming you would just use a loop to handle repeating the generation and classification.
# For or while loops make that simple without extra work. If someone tried to get ten readings by copying the block each time it would end up messy though. 
# The file gets bigger fast with all the repeated parts and changing anything later means fixing it everywhere which is easy to mess up. 
# It seems like that is not how things are really done. I think most people would avoid it for that reason.
# ==============================================================================
