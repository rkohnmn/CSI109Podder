# Filter rows above 25 C into hot_days.csv

infile = open("readings.csv", "r")
outfile = open("hot_days.csv", "w")

# Preserve the header
header = infile.readline()
outfile.write(header)

# Write only rows where temp is above 25
count = 0
for line in infile:
    fields = line.strip().split(",")
    temp = float(fields[3])
    if temp > 25:
        outfile.write(line)
        count += 1

infile.close()
outfile.close()

print(f"Rows kept: {count}")

