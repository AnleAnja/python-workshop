import random

geheime_zahl = random.randint(1, 100)
versuche = 0
tipps = []

print("Willkommen zum Zahlenratespiel!")
print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Kannst du sie erraten?")

while True:
    tipp = int(input("Gib deinen Tipp ein: "))
    versuche += 1
    tipps.append(tipp)

    if tipp < geheime_zahl:
        print("Zu niedrig! Versuche es nochmal.")
    elif tipp > geheime_zahl:
        print("Zu hoch! Versuche es nochmal.")
    else:
        print(f"\nHerzlichen Glückwunsch! Du hast die Zahl {geheime_zahl} erraten!")
        print(f"Du hast {versuche} Versuche gebraucht.")
        print(f"Deine bisherigen Tipps waren: {tipps}")
        break