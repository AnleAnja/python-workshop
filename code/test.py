werte = [" 1,23", "4, 56 ", " 7,89"]
# ziel: [1.23, 4.56, 7.89]

def bereinige(wert):
    return float(wert.strip().replace(",", ".").replace(" ", ""))

ziel = [bereinige(w) for w in werte]

print(sum(ziel) / len(ziel))