# Append current date and time to log.txt each run

import datetime

now = datetime.datetime.now()
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

log = open("log.txt", "a")
log.write(f"Program ran at: {timestamp}\n")
log.close()

print(f"Logged: {timestamp}")

