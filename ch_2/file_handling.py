# opening a file:
#file_objejct=open(filename,mode)
#mode: r-read w-write a-append x-create a new file

# Basic read (best practice)
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Line by line
with open("file.txt") as f:
    for line in f:
        print(line.strip())

# Write (wipes)
with open("file.txt", "w") as f:
    f.write("Hello\n")

# Append
with open("file.txt", "a") as f:
    f.write("More\n")

# CSV
import csv
with open("data.csv", "w", newline="") as f:
    csv.writer(f).writerow(["a", "b"])

# JSON
import json
with open("data.json", "w") as f:
    json.dump({"x": 1}, f)

# Check exists
import os
if os.path.exists("file.txt"):
    ...

# Error handling
try:
    with open("file.txt") as f:
        content = f.read()
except FileNotFoundError:
    print("Missing file")