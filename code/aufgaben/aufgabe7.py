import csv

quiz_datei = "aufgabe7-input.csv"

richtige_antworten_zaehler = 0
anzahl_fragen = 0

with open(quiz_datei, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, frage_daten in enumerate(reader):
        anzahl_fragen += 1

        print(f"\nFrage {i + 1}: {frage_daten['Frage']}")
        print(f"A) {frage_daten['OptionA']}")
        print(f"B) {frage_daten['OptionB']}")
        print(f"C) {frage_daten['OptionC']}")

        benutzer_antwort = input("Deine Antwort (A, B oder C): ").upper()

        korrekte_antwort = frage_daten['KorrekteAntwort']
        if benutzer_antwort == korrekte_antwort:
            print("Richtig!")
            richtige_antworten_zaehler += 1
        else:
            print(f"Falsch! Die richtige Antwort war {korrekte_antwort}.")

print("\n--- Quiz-Ergebnis ---")
print(f"Du hast {richtige_antworten_zaehler} von {anzahl_fragen} Fragen richtig beantwortet.")
print("--------------------")