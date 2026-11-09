# Write a summary report to report.txt

file = open("readings.csv", "r")

# Skip the header
file.readline()

# Build totals and counts per station and overall
totals = {}
counts = {}
overall_total = 0
overall_count = 0
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
    overall_total += temp
    overall_count += 1

file.close()

# Write the report
report = open("report.txt", "w")

report.write(f"Number of records: {overall_count}\n")
report.write(f"Overall mean temp: {overall_total / overall_count:.2f} C\n")
report.write("\nPer-station mean:\n")
for code in sorted(totals.keys()):
    mean = totals[code] / counts[code]
    report.write(f"  {code}: {mean:.2f} C ({counts[code]} readings)\n")

report.close()

print("Report written to report.txt")

