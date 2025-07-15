import csv

eingabe_datei = "aufgabe6-input.csv"
ausgabe_datei = "aufgabe6-output.csv"

ergebnisse = []

with open(eingabe_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        student_id = zeile["StudentID"]
        aufgabe1 = int(zeile["Aufgabe1"])
        aufgabe2 = int(zeile["Aufgabe2"])
        klausur = int(zeile["Klausur"])

        endpunktzahl = (aufgabe1 * 0.25) + (aufgabe2 * 0.25) + (klausur * 0.50)

        endnote = ""
        if endpunktzahl > 90:
            endnote = "A"
        elif endpunktzahl > 80:
            endnote = "B"
        elif endpunktzahl > 70:
            endnote = "C"
        elif endpunktzahl > 60:
            endnote = "D"
        else:
            endnote = "F"

        ergebnisse.append({
            "StudentID": student_id,
            "Endpunktzahl": f"{endpunktzahl:.2f}", # Formatieren auf 2 Dezimalstellen
            "Endnote": endnote
        })

with open(ausgabe_datei, 'w', newline='', encoding='utf-8') as f:
    feldnamen = ["StudentID", "Endpunktzahl", "Endnote"]
    writer = csv.DictWriter(f, fieldnames=feldnamen)

    writer.writeheader()
    writer.writerows(ergebnisse)

print(f"Zeugnisse wurden in '{ausgabe_datei}' erstellt.")