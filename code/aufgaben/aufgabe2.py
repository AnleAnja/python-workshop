log_datei = "aufgabe2-input.log"
fehler_datei = "aufgabe2-output.log"

log_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_messages = []

with open(log_datei, encoding='utf-8') as f:
    for zeile in f:
        teile = zeile.split(" - ")
        if len(teile) >= 2:
            level = teile[1]

            if level in log_counts:
                log_counts[level] += 1

                if level == "ERROR":
                    error_messages.append(zeile)

print("Log-Level-Zählungen:")
print(f"INFO: {log_counts['INFO']}")
print(f"WARNING: {log_counts['WARNING']}")
print(f"ERROR: {log_counts['ERROR']}")
print("-" * 20)

benutzer_level = input("Nach welchem Log-Level möchten Sie filtern? (INFO, WARNING, ERROR): ")
benutzer_level = benutzer_level.upper()

print(f"\nNachrichten für Level '{benutzer_level}':")
with open(log_datei, encoding='utf-8') as f:
    for zeile in f:
        teile = zeile.split(" - ")
        if len(teile) >= 2:
            level = teile[1]
            if level == benutzer_level:
                print(zeile.strip())

with open(fehler_datei, 'w', encoding='utf-8') as f:
    for msg in error_messages:
        f.write(msg)

print(f"\nAlle ERROR-Meldungen wurden in '{fehler_datei}' geschrieben.")