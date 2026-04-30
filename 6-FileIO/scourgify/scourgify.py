import csv
import sys

rows = []
filename = sys.argv[1]

if not filename.lower().endswith(".csv"):
    sys.exit("Not a csv")
try:
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            last, first = [part.strip() for part in row["name"].split(",")]
            rows.append({"first": first, "last": last, "house": row["house"].strip()})
except FileNotFoundError:
    sys.exit("File does not exist")
