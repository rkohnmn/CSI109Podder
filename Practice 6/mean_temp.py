# Cast temperature values and compute the mean temp

file = open("readings.csv", "r")

# Skip the header
file.readline()

# Total up all temperatures
total = 0
count = 0
for line in file:
    fields = line.strip().split(",")
    temp = float(fields[3])
    total += temp
    count += 1

file.close()

# Calculate and display the mean
mean_temp = total / count
print(f"Number of readings: {count}")
print(f"Mean temperature: {mean_temp:.2f} C")

