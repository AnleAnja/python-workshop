import os, csv

for datei in os.listdir("csvs/"):
    if datei.endswith(".csv"):
        with open("csvs/" + datei, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for zeile in reader:
                if float(zeile["Temperatur"]) > 30:
                    print("Warnung:", zeile)