# Übung: Fuzzy-Join von Excel-Tabellen

In dieser Übung sollen zwei Excel-Dateien anhand der Spalte **"Geschäftsprozess-Name"** zusammengeführt werden.  

**Ziel:**  
- Einen **inneren Join** durchführen, wobei die Strings nicht exakt übereinstimmen, sondern mit **RapidFuzz** gefuzzy-matched werden.  
- Nur Matches mit einem **Score ≥ 80** gelten als Übereinstimmung.  

**Dateien:**  

1. **Tabelle_1.xlsx**  

| Geschäftsprozess-Name        | Zugehörige IT-Anwendung | Risikobewertung der IT-Anwendung |
|------------------------------|------------------------|---------------------------------|
| EP: Inland Zahlungsverkehr    | ABC                    | Niedrig                         |
| EP: Inland Zahlungsverkehr    | DEF                    | Hoch                            |
| EP: SEPA  Zahlungsverkehr     | XYZ                    | Mittel                          |
| EP: SEPA  Zahlungsverkehr     | GHI                    | Niedrig                         |
| EP: SEPA  Zahlungsverkehr     | JKL                    | Niedrig                         |

2. **Tabelle_2.xlsx**  

| Geschäftsprozess-Name            | Process Owner des Geschäftsprozesses |
|---------------------------------|-------------------------------------|
| A1.01.09 Inlands-Zahlungsverkehr | Frau Müller                        |
| A1.01.10 SEPA-Zahlungsverkehr    | Herr Meier                          |

## Aufgabenstellung:
1. Lese beide Excel-Dateien in Pandas DataFrames ein.  
2. Vergleiche die Spalte **"Geschäftsprozess-Name"** zwischen beiden DataFrames.  
3. Führe einen **inneren Join** durch, indem du die Zeilen zusammenführst, deren Geschäftsprozess-Namen **gut zueinander passen** (Fuzzy-Matching Score ≥ 80).  
4. Erstelle ein neues DataFrame mit folgenden Spalten:  

- Geschäftsprozess-Name (aus Tabelle 1)  
- Zugehörige IT-Anwendung  
- Risikobewertung der IT-Anwendung  
- Process Owner des Geschäftsprozesses  

5. Speichere das Ergebnis in eine neue Excel-Datei `Fuzzy_Join_Ergebnis.xlsx`.  
