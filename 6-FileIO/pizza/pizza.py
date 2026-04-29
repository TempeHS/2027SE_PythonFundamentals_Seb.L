import csv
from pprint import pprint
from tabulate import tabulate
import sys

rows = []
filename = sys.argv[1]

if not filename.lower().endswith(".csv"):
    sys.exit("Not a csv")
try:
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
except FileNotFoundError:
    sys.exit("File doesnt exist")

print(tabulate(rows, headers="keys", tablefmt="grid"))
