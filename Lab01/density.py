"""
Author: Robert Thomas Kohn
Date: September 12, 2026
Description: Computes the population density of Allentown and prints a report.
Code of honesty: I have not copied from any source without proper citation.
"""

# City info.
city_name = "Allentown"       # string
city_population = 121547      # int
city_area_sq_km = 46.6        # float

# Density = population / area.
population_density = city_population / city_area_sq_km

# Print the report.
print(f"City: {city_name}")
print(f"Population: {city_population}")
print(f"Area (sq km): {city_area_sq_km}")
print(f"Density: {population_density:.2f} per sq km")

# Print the types.
print(f"Types: {type(city_name)} {type(city_population)} {type(city_area_sq_km)}")
