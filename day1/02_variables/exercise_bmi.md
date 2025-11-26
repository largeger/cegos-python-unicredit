# 📝 Aufgabe: BMI-Rechner in Python

Erstelle ein Python-Programm, das den Body-Mass-Index (BMI) einer Person berechnet und anschließend die passende Kategorie ausgibt.  
Der Benutzer soll **Name**, **Größe** (in Metern) und **Gewicht** (in Kilogramm) eingeben.

## Teil 1 (Kapitel "Variablen"): Berechnung des BMI

Schreibe ein Programm, das:

1. Den Benutzer nach **Name**, **Größe in Metern** (z. B. 1.78) und **Gewicht in Kilogramm** fragt.  
2. Den BMI nach folgender Formel berechnet:  
BMI = Gewicht / (Größe²)

3. Den BMI mit **zwei Nachkommastellen** ausgibt.

## Teil 2 (Kapitel "Kontrollstrukturen"): Einordnung des BMI

Erweitere das Programm so, dass es abhängig vom BMI-Wert die passende Kategorie ausgibt:

| BMI-Bereich | Kategorie        |
|-------------|------------------|
| < 18.5      | Untergewicht     |
| 18.5–24.9   | Normalgewicht    |
| 25–29.9     | Übergewicht      |
| ≥ 30        | Adipositas       |

Das Programm soll nach der Berechnung automatisch die Kategorie anzeigen.
