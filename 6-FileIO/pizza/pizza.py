import csv
from pprint import pprint

rows = []
for filename in ("sicilian.csv", "regular.csv"):
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

print(f"Loaded {len(rows)} rows")
pprint(rows[:3])
