# Compute mean temperature per station using two dictionaries

file = open("readings.csv", "r")

# Skip the header
file.readline()

# Build totals and counts per station
totals = {}
counts = {}
for line in file:
    fields = line.strip().split(",")
    station = fields[0]
    temp = float(fields[3])
    if station in totals:
        totals[station] += temp
        counts[station] += 1
    else:
        totals[station] = temp
        counts[station] = 1

file.close()

# Print mean temps sorted by station code
for code in sorted(totals.keys()):
    mean = totals[code] / counts[code]
    print(f"{code}: {mean:.2f} C")

