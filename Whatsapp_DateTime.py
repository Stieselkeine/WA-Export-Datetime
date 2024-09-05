# open chat test-file in current folder with the name given by argument 0

import sys
import os
import re
from datetime import datetime

# check if the file name is given as argument
if len(sys.argv) < 2:
    print("Please provide the file name as argument")
    sys.exit()

# open the file
file_name = sys.argv[1]
try:
    file = open(file_name, "r", errors="ignore", encoding="utf-8")
except:
    print("File not found")
    sys.exit()

# read the file
lines = file.readlines()
file.close()

#print(lines)

#filter only lines that contain media files
regex_line_filter = re.compile(r".*(IMG|VID)-\d{8}-WA\d{4}.(jpg|mp4) \(Datei angehängt\)")
filtered_lines = list(filter(regex_line_filter.match, lines))
print(str(len(filtered_lines)) + " media files found")



for line in filtered_lines:
    try:
        date = datetime.strptime(line[:15], "%d.%m.%y, %H:%M")
    except:
        print("Error parsing date in: " + line)
        continue

    filename = line[-42:-19]
    try:
        os.utime(filename, (date.timestamp(), date.timestamp()))
    except:
        print("Error setting timestamp for: " + filename)
        continue


