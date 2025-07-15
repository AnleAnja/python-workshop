import csv

wetter_datei = "aufgabe5-input.csv"

max_temperaturen = []
tage_mit_niederschlag = 0
heissester_tag_datum = ""
hoechste_max_temp = -1000

with open(wetter_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        datum = zeile["Datum"]
        max_temp = int(zeile["MaxTemp"])
        niederschlag = float(zeile["Niederschlag_mm"])

        max_temperaturen.append(max_temp)

        if max_temp > hoechste_max_temp:
            hoechste_max_temp = max_temp
            heissester_tag_datum = datum

        if niederschlag > 0:
            tage_mit_niederschlag += 1

durchschnittstemperatur = sum(max_temperaturen) / len(max_temperaturen)

print("--- Wetterbericht ---")
print(f"Zeitraum: {len(max_temperaturen)} Tage")
print(f"Durchschnittliche Max-Temperatur: {durchschnittstemperatur:.2f}°C") # Formatiert auf 2 Dezimalstellen
print(f"Heißester Tag: {heissester_tag_datum} mit {hoechste_max_temp}°C")
print(f"Anzahl der Tage mit Niederschlag: {tage_mit_niederschlag}")
print("---------------------")