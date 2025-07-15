import csv

transaktionen_datei = "aufgabe3-input.csv"

alle_transaktionen = []
gesamt_einnahmen = 0
gesamt_ausgaben = 0

with open(transaktionen_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        alle_transaktionen.append(zeile)
        betrag = int(zeile["Betrag"])
        if zeile["Typ"] == "Einnahme":
            gesamt_einnahmen += betrag
        else:
            gesamt_ausgaben += betrag

kontostand = gesamt_einnahmen - gesamt_ausgaben

print(f"Aktuelle Bilanz:")
print(f"  Einnahmen: {gesamt_einnahmen}")
print(f"  Ausgaben:  {gesamt_ausgaben}")
print(f"  Kontostand: {kontostand}")
print("-" * 20)

while True:
    aktion = input("Möchten Sie eine neue Transaktion hinzufügen? (ja/nein)").lower()

    if aktion == "nein":
        break

    if aktion == "ja":
        neues_datum = input("Datum (YYYY-MM-DD): ")
        neue_beschreibung = input("Beschreibung: ")
        neuer_typ = input("Typ (Einnahme/Ausgabe): ").capitalize()
        neuer_betrag_str = input("Betrag: ")
        neuer_betrag = int(neuer_betrag_str)

        neue_transaktion = {
            "Datum": neues_datum,
            "Beschreibung": neue_beschreibung,
            "Typ": neuer_typ,
            "Betrag": str(neuer_betrag)
        }
        alle_transaktionen.append(neue_transaktion)

        if neuer_typ == "Einnahme":
            gesamt_einnahmen += neuer_betrag
        else:
            gesamt_ausgaben += neuer_betrag
        kontostand = gesamt_einnahmen - gesamt_ausgaben

        print(f"Transaktion hinzugefügt. Neuer Kontostand: {kontostand}")

    else:
        print("Ungültige Eingabe. Bitte 'ja' oder 'nein' eingeben.")

with open(transaktionen_datei, 'w', newline='', encoding='utf-8') as f:
    feldnamen = ["Datum", "Beschreibung", "Typ", "Betrag"]
    writer = csv.DictWriter(f, fieldnames=feldnamen)

    writer.writeheader()
    writer.writerows(alle_transaktionen)

print("Budget-Tracker beendet. Alle Transaktionen wurden gespeichert.")