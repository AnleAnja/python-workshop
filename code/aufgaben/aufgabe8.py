artikel_datei = "aufgabe8-input.txt"

with open(artikel_datei, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.lower()

satzzeichen = ['.', ',', ';', '!', '?', ':', '"', "'", '(', ')']
for zeichen in satzzeichen:
    text = text.replace(zeichen, ' ')

woerter = text.split()

wort_haeufigkeit = {}

for wort in woerter:
    if wort in wort_haeufigkeit:
        wort_haeufigkeit[wort] += 1
    else:
        wort_haeufigkeit[wort] = 1

print("--- Worthäufigkeiten ---")
for wort, haeufigkeit in wort_haeufigkeit.items():
    print(f"'{wort}': {haeufigkeit}")
print("----------------------")