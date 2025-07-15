import csv

with open("daten.csv", newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        print(zeile["Name"], zeile["Umsatz"])
