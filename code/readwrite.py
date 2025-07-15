with open("daten.txt", "r", encoding="utf-8") as f:
    for zeile in f:
        print(zeile.strip())

with open("berichte/ausgabe.txt", "w", encoding="utf-8") as f:
    f.write("Hallo Welt!\n")