import csv

eingabe_datei = "aufgabe4-input.csv"
ausgabe_datei = "aufgabe4-output.csv"

alle_mitarbeiter = []
with open(eingabe_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        alle_mitarbeiter.append(zeile)

gewuenschte_abteilung = input("Nach welcher Abteilung soll gefiltert werden? (z.B. Entwicklung, Marketing): ")

mitarbeiter_nach_abteilung = []
for mitarbeiter in alle_mitarbeiter:
    if mitarbeiter["Abteilung"].lower() == gewuenschte_abteilung.lower():
        mitarbeiter_nach_abteilung.append(mitarbeiter)

mindest_dienstjahre = int(input("Welche Mindestanzahl an Dienstjahren soll berücksichtigt werden? "))

final_gefilterte_mitarbeiter = []
for mitarbeiter in mitarbeiter_nach_abteilung:
    dienstjahre = int(mitarbeiter["Dienstjahre"])
    if dienstjahre >= mindest_dienstjahre:
        final_gefilterte_mitarbeiter.append(mitarbeiter)

with open(ausgabe_datei, 'w', newline='', encoding='utf-8') as f:
    feldnamen = ["MitarbeiterID", "Name", "Abteilung", "Dienstjahre"]
    writer = csv.DictWriter(f, fieldnames=feldnamen)

    writer.writeheader()
    writer.writerows(final_gefilterte_mitarbeiter)

print(f"Gefilterte Mitarbeiterliste wurde in '{ausgabe_datei}' gespeichert.")