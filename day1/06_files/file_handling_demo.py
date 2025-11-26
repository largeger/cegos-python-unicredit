# ============================================
#   Python File Handling & Ordner Navigation
# ============================================

import os

# -------- 1. Lesen einer Textdatei --------
datei_pfad = "day1/06_files/"

try:
    with open(datei_pfad+"beispiel.txt", "r", encoding="utf-8") as datei:
        inhalt = datei.read()
        print("Inhalt der Datei:")
        print(inhalt)
except FileNotFoundError:
    print(f"Datei {datei_pfad} wurde nicht gefunden.")

# -------- 2. Schreiben in eine Textdatei --------
text_zum_schreiben = "Eigschnabbda, Bettbrunza, junga Hubbfa, Grachal, Gibskobf, Gschaftlhuber, Bettbrunza, Kittlschliaffa, Doafdrottl, Dramhappada, schleich di, krummhaxata Goaßbog, du bist doch af da Brennsuppn daheagschwomma, Hundsbua, Radlfahra, Zipfebritschn, Zeeefix, Flaschn, Kasberl, Saubreiß, Drietschla, Blattada, hoit’s Mei, krummhaxata Goaßbog, Aufmüpfiga, Ratschkathl, Zigarettnbiaschal, du Ams’l, du bleede, Schnoin, Badhur, Freindal, Halbkreisingeneur, Zeeefix, Betonschedl, Heislschleicha, Hallodri, Hoibschaariga, Zigarettnbiaschal, Kasberlb, Schoaswiesn."

with open(datei_pfad+"ausgabe.txt", "w", encoding="utf-8") as datei:
    datei.write(text_zum_schreiben)
    print("\nText erfolgreich in 'ausgabe.txt' geschrieben.")

# -------- 3. Anhängen an eine Datei --------
mit_anhang = "\nDies ist eine angehängte Zeile."
with open(datei_pfad+"ausgabe.txt", "a", encoding="utf-8") as datei:
    datei.write(mit_anhang)
    print("Text erfolgreich angehängt.")

# -------- 4. Navigieren durch Ordnerstrukturen --------
aktueller_ordner = os.getcwd()
print(f"\nAktueller Ordner: {aktueller_ordner}")

# Alle Dateien und Ordner im aktuellen Verzeichnis auflisten
print("\nInhalt des aktuellen Ordners:")
for eintrag in os.listdir(aktueller_ordner):
    pfad = os.path.join(aktueller_ordner, eintrag)
    if os.path.isfile(pfad):
        print(f"Datei: {eintrag}")
    elif os.path.isdir(pfad):
        print(f"Ordner: {eintrag}")

# -------- 5. Unterordner betreten --------
unterordner = "day1"
if os.path.exists(unterordner) and os.path.isdir(unterordner):
    os.chdir(unterordner)
    print(f"\nJetzt im Unterordner: {os.getcwd()}")
else:
    print(f"\nUnterordner '{unterordner}' existiert nicht.")
