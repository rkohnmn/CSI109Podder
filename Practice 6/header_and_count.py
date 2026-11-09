# Consume header with readline(), print as list, count remaining rows

file = open("readings.csv", "r")

# Read and display the header as a list
header = file.readline().strip()
columns = header.split(",")
print("Header:", columns)

# Count the remaining rows
count = 0
for line in file:
    count += 1

file.close()

print(f"Number of data rows: {count}")

