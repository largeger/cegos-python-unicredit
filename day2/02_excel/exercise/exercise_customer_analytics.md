# Übungsaufgabe: Verkaufs- und Kundenanalyse aus mehreren Excel-Dateien


## Szenario
Du arbeitest für ein E-Commerce-Unternehmen. Du erhältst jeden Monat zwei Excel-Dateien:


1. **Verkaufsdateien** (z. B. `verkaeufe_jan.xlsx`, `verkaeufe_feb.xlsx`) mit Spalten:
- Bestell-ID
- Produkt
- Menge
- Preis


2. **Kundendateien** (z. B. `kunden_jan.xlsx`, `kunden_feb.xlsx`) mit Spalten:
- Bestell-ID
- Kunde
- Stadt
- Treueprogramm


Die Aufgabe ist, die Daten aus allen Excel-Dateien zusammenzuführen und Analysen durchzuführen.


## Aufgaben

### Aufgabe A: Daten vorbereiten
- Erstelle mehrere kleine Excel-Dateien mit jeweils 3-5 Zeilen Beispieldaten.

### Aufgabe B: Mehrere Dateien einlesen
- Verwende `glob` oder `os`, um alle Verkaufsdateien zu laden und untereinander zu verbinden.

### Aufgabe C: Kundendaten einlesen
- Lade alle Kundendateien und füge sie zusammen.

### Aufgabe D: Daten zusammenführen
- Merge Verkaufs- und Kundendaten auf `Bestell-ID` mit `how='inner'`.

### Aufgabe E: Analyse
- Berechne Umsatz pro Kunde (`Umsatz = Preis * Menge`).
- Zeige die Top 3 Kunden nach Umsatz.
- Berechne Gesamtumsatz pro Stadt.

### Aufgabe F: Ergebnisse in Excel speichern
- Speichere die zusammengeführten Daten in eine neue Excel-Datei `zusammengefuehrte_daten.xlsx`.
- Style die Tabelle z. B. mit Fettschrift für Header, Rahmen oder Zellfarben.

### Bonusaufgabe
- Füge eine Spalte `Treuebonus` hinzu (5% für Treueprogramm = Ja).
- Berechne bereinigten Umsatz nach Bonus.