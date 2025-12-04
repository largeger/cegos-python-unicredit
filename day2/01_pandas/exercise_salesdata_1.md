# 🧩 Pandas Challenge #1: Verkaufsdaten-Analyse

## 1. Vorbereitung (Datensatz erstellen)
Kopiere diesen Code in dein Notebook/Skript, um den Start-Datensatz zu erzeugen. Er enthält absichtlich ein paar "Probleme" (fehlende Werte), die du beheben musst.

```python
import pandas as pd
import numpy as np

data = {
    'Datum': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-04'],
    'Produkt': ['Laptop', 'Maus', 'Monitor', 'Laptop', 'Tastatur', 'Maus'],
    'Kategorie': ['Elektronik', 'Zubehör', 'Elektronik', 'Elektronik', 'Zubehör', 'Zubehör'],
    'Preis': [1200, 25, 300, 1200, np.nan, 25], # Ein fehlender Preis
    'Menge': [1, 10, 2, 1, 5, 12],
    'Stadt': ['Berlin', 'München', 'Berlin', 'Hamburg', 'Berlin', 'München']
}

df = pd.DataFrame(data)
```

## 2. ⚡ Deine Mission

### Aufgabe A: Erster Überblick 📺
1. Lass dir die ersten 5 Zeilen des DataFrames anzeigen.
2. Prüfe die Datentypen und ob es fehlende Werte gibt (nutze info()).
3. Lass dir die statistischen Kennzahlen (Durchschnitt, Min, Max) der numerischen Spalten anzeigen.

### Aufgabe B: Datenbereinigung 🧹
1. Du hast festgestellt, dass in der Spalte Preis ein Wert fehlt (NaN). 
    - Szenario: Wir wissen, dass die Tastatur 45 Euro kostet. Fülle den fehlenden Wert also mit 45.0.

2. Konvertiere die Spalte Datum in ein echtes datetime-Objekt (siehe Cheat Sheet Punkt 10).

### Aufgabe C: Datenmanipulation (Feature Engineering) 🧰
1. Erstelle eine neue Spalte Umsatz.
    - Formel: Umsatz = Preis * Menge.

### Aufgabe D: Analyse & Filterung 🔎
1. Filtere den DataFrame: Zeige alle Verkäufe an, die in Berlin getätigt wurden.
2. Welcher Verkauf hatte den höchsten Umsatz? Zeige die entsprechende Zeile an.

### Aufgabe E: Gruppierung & Aggregation 📊
1. Berechne den Gesamtumsatz pro Stadt.
2. Berechne, wie viel Stück (Menge) von jeder Kategorie verkauft wurden.