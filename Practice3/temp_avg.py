# Collect temperature readings until the user types "done"
total = 0
count = 0

reading = input("Enter a temperature (or 'done' to finish): ")

while reading.lower() != "done":
    total = total + float(reading)
    count = count + 1
    reading = input("Enter a temperature (or 'done' to finish): ")

# Print results or handle no readings
if count == 0:
    print("No readings were entered.")
else:
    average = total / count
    print(f"Number of readings: {count}")
    print(f"Average temperature: {average:.2f}")
