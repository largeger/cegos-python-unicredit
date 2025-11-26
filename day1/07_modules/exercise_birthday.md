# Übung: Geburtsdatum analysieren

## Aufgabe

Schreibe ein Python-Programm, das folgende Aufgaben erledigt:

1. **Eingabe:**  
   Der Benutzer soll sein Geburtsdatum im Format `TT.MM.JJJJ` eingeben.

2. **Berechnungen:**  
   - Berechne das aktuelle Alter der Person in Jahren.  
   - Bestimme den Wochentag, an dem die Person geboren wurde.  
   - Berechne, wie viele Tage bis zum nächsten Geburtstag noch verbleiben.

3. **Ausgabe:**  
   Gib die Ergebnisse in einem übersichtlichen Text aus, z.B.:

```
Du bist 27 Jahre alt.
Du wurdest an einem Dienstag geboren.
Es sind noch 123 Tage bis zu deinem nächsten Geburtstag.
```

## Hinweise

- Verwende das Modul `datetime`.  
- Achte auf die richtige Behandlung von Schaltjahren.  
- Nutze `datetime.strptime()` zur Umwandlung der Eingabe in ein Datum.
