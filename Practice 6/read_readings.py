# Read and display contents of readings.csv

file = open("readings.csv", "r")
contents = file.read()
file.close()

print(contents)

