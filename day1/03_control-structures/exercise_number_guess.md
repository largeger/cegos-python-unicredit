# Aufgabe: Zahlen-Ratespiel in Python

## Ziel
Schreibe ein kleines Zahlen-Ratespiel in Python. Das Spiel soll es dem Benutzer ermöglichen, eine zufällig generierte Zahl zu erraten.

## Anforderungen

1. **Zufällige Zahl**
   - Das Programm soll eine zufällige Zahl zwischen **1** und **10** generieren.
   - Verwende dafür das Python-Modul `random`.

2. **Benutzereingabe**
   - Der Benutzer hat **3 Versuche**, um die Zahl zu erraten.
   - Nach jeder Eingabe soll das Programm prüfen, ob der Tipp korrekt ist.

3. **Richtungs-Hinweise**
   - Wenn der Tipp **zu niedrig** ist, soll ausgegeben werden:  
     `Zu niedrig! Versuch es höher.`
   - Wenn der Tipp **zu hoch** ist, soll ausgegeben werden:  
     `Zu hoch! Versuch es niedriger.`

4. **Ergebnis**
   - Bei richtigem Tipp:  
     `🎉 Glückwunsch! Du hast die Zahl erraten!`
   - Wenn alle Versuche aufgebraucht sind:  
     `Leider verloren! Die richtige Zahl war <zufallszahl>.`

5. **Struktur**
   - Nutze eine `while`-Schleife, um die Versuche zu zählen.
   - Alle Ausgaben erfolgen über `print()`.
   - Eingaben werden mit `input()` abgefragt.

## Bonus (optional)
- Füge eine Begrüßung mit Namen des Benutzers hinzu.
- Erlaube dem Benutzer, das Spiel mehrfach zu spielen.
