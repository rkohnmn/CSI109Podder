# Print the first five lines of readings.csv without newlines

file = open("readings.csv", "r")
lines = file.readlines()
file.close()

for i in range(5):
    print(lines[i].strip())

