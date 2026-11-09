# Count how many rows belong to station ALN

file = open("readings.csv", "r")

# Skip the header
file.readline()

count = 0
for line in file:
    fields = line.strip().split(",")
    station = fields[0]
    if station == "ALN":
        count += 1

file.close()

print(f"ALN rows: {count}")

