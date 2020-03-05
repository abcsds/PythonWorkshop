import csv


path = "./data/exceptions.csv"
with open(path, 'r', encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Setup a csv reader
    for i, row in enumerate(reader):  # Iterate over every row
        print(f"Row: {i}, {row}")  # Print every row
