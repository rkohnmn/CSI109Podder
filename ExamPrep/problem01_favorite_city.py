# Favorite city information
city = input("Enter the name of your favorite city: ")

# Calculate and display the required outputs
print("Number of characters:", len(city))
print("City name in uppercase:", city.upper())
print("City name in lowercase:", city.lower())
if len(city) > 0:
    print("First character:", city[0])
