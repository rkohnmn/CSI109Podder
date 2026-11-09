# Compute mean temperature per date using two dictionaries

file = open("readings.csv", "r")

# Skip the header
file.readline()

# Build totals and counts per date
totals = {}
counts = {}
for line in file:
    fields = line.strip().split(",")
    date = fields[2]
    temp = float(fields[3])
    if date in totals:
        totals[date] += temp
        counts[date] += 1
    else:
        totals[date] = temp
        counts[date] = 1

file.close()

# Print mean temps sorted by date
for date in sorted(totals.keys()):
    mean = totals[date] / counts[date]
    print(f"{date}: {mean:.2f} C")

