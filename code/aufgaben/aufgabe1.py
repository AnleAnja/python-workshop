import csv

eingabe_datei = "aufgabe1-input.csv"
ausgabe_datei = "aufgabe1-output.txt"

gesamt_umsatz = 0
produkt_verkaeufe = {} # Speichert: ProduktName -> Gesamt verkaufte Einheiten

with open(eingabe_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
            verkaufte_einheiten = int(zeile["VerkaufteEinheiten"])
            preis_pro_einheit = int(zeile["PreisProEinheit"])
            produkt_name = zeile["ProduktName"]

            umsatz_dieser_zeile = verkaufte_einheiten * preis_pro_einheit
            gesamt_umsatz += umsatz_dieser_zeile

            if produkt_name in produkt_verkaeufe:
                produkt_verkaeufe[produkt_name] += verkaufte_einheiten
            else:
                produkt_verkaeufe[produkt_name] = verkaufte_einheiten

bestes_produkt = ""
max_verkauft = -1

for produkt, verkaufte in produkt_verkaeufe.items():
    if verkaufte > max_verkauft:
        max_verkauft = verkaufte
        bestes_produkt = produkt

if not bestes_produkt:
    bestes_produkt = "Keine Produkte gefunden"

with open(ausgabe_datei, 'w', encoding='utf-8') as f:
    f.write(f"Gesamtumsatz: {gesamt_umsatz}\n")
    f.write(f"Bestverkauftes Produkt (nach Einheiten): {bestes_produkt}\n")

print(f"Analyse abgeschlossen. Bericht wurde in '{ausgabe_datei}' gespeichert.")