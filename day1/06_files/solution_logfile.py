# ============================================
# Logfile auslesen und auswerten in Python
# ============================================

# Modul für Counter (nützlich für Statuscodes)
from collections import Counter

# -------------------------
# 1. Logfile einlesen
# -------------------------
file_path = "day1/06_files/"
logfile = file_path + "access.log"
errorfile = file_path + "errors.log"

try:
    with open(logfile, "r", encoding="utf-8") as datei:
        zeilen = datei.readlines()
        print(f"Es wurden {len(zeilen)} Zeilen aus '{logfile}' eingelesen.")
except FileNotFoundError:
    print(f"Fehler: Die Datei '{logfile}' wurde nicht gefunden.")
    exit(1)  # Programm abbrechen, wenn Datei nicht existiert

# -------------------------
# 2. IP-Adressen extrahieren
# -------------------------
ip_adressen = set()  # Set für eindeutige IPs
for zeile in zeilen:
    teile = zeile.split()
    if len(teile) > 0:
        ip_adressen.add(teile[0])  # IP-Adresse steht in der ersten Spalte

# Ausgabe der eindeutigen IP-Adressen
print("\nEindeutige IP-Adressen:")
for ip in ip_adressen:
    print(f"- {ip}")

# -------------------------
# 3. HTTP-Status auswerten
# -------------------------
status_counter = Counter()  # Dictionary-ähnlich, zählt automatisch

for zeile in zeilen:
    teile = zeile.split()
    if len(teile) >= 9:  # Statuscode steht normalerweise an 9. Stelle
        status = teile[8]
        status_counter[status] += 1

# Ausgabe der Statuscodes
print("\nHTTP-Statuscodes:")
for status, anzahl in status_counter.items():
    print(f"Status {status}: {anzahl} mal")

# -------------------------
# 4. Bonus: Fehlercodes >= 400 extrahieren
# -------------------------
fehler_zeilen = [zeile for zeile in zeilen if len(zeile.split()) >= 9 and int(zeile.split()[8]) >= 400]

if fehler_zeilen:
    with open(errorfile, "w", encoding="utf-8") as fehler_datei:
        fehler_datei.writelines(fehler_zeilen)
    print(f"\nEs wurden {len(fehler_zeilen)} fehlerhafte Einträge in 'errors.log' gespeichert.")
else:
    print("\nKeine fehlerhaften Einträge gefunden.")

# -------------------------
# Optional: IP-Adresse mit den meisten Zugriffen
# -------------------------
ip_counter = Counter()
for zeile in zeilen:
    teile = zeile.split()
    if len(teile) > 0:
        ip_counter[teile[0]] += 1

max_ip = ip_counter.most_common(1)
if max_ip:
    print(f"\nIP-Adresse mit den meisten Zugriffen: {max_ip[0][0]} ({max_ip[0][1]} Zugriffe)")
