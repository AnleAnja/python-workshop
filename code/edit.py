import os

for datei in os.listdir("berichte/"):
    if datei.endswith(".txt"):
        neu = datei.replace(" ", "_")
        os.rename("berichte/" + datei, "berichte/" + neu)
