def bereinige(wert):
    return float(wert.strip().replace(",", "."))

werte = [" 1,23", "4,56 ", " 7,89"]
bereinigt = [bereinige(w) for w in werte]
print(sum(bereinigt) / len(bereinigt))
