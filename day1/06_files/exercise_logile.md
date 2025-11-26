# Übung: Auslesen und Auswerten eines Logfiles in Python

## Ziel
Ein Logfile enthält Einträge über Zugriffe auf einen Webserver. Die Aufgabe besteht darin, die Datei einzulesen, bestimmte Informationen zu extrahieren und auszuwerten.

## Voraussetzungen
- Grundkenntnisse in Python
- Umgang mit Dateien (`open`, `read`, `with`)
- Strings bearbeiten (z. B. `split`, `strip`)

## Beispiel für ein Logfile (`access.log`)
```
192.168.1.2 - - [25/Nov/2025:10:12:45 +0100] "GET /index.html HTTP/1.1" 200
192.168.1.3 - - [25/Nov/2025:10:15:22 +0100] "POST /login HTTP/1.1" 401
192.168.1.2 - - [25/Nov/2025:10:18:10 +0100] "GET /about.html HTTP/1.1" 200
192.168.1.4 - - [25/Nov/2025:10:20:03 +0100] "GET /contact.html HTTP/1.1" 404
```

## Aufgabenstellung
1. **Logfile einlesen**
   - Öffne die Datei `access.log` und lese alle Zeilen ein.

2. **IP-Adressen extrahieren**
   - Sammle alle eindeutigen IP-Adressen, die im Log auftauchen.

3. **HTTP-Status auswerten**
   - Zähle, wie oft jeder HTTP-Statuscode (z. B. 200, 401, 404) vorkommt.

4. **Ergebnisse ausgeben**
   - Drucke die Liste der eindeutigen IP-Adressen.
   - Gib die Anzahl der Vorkommen jedes Statuscodes aus.

## Bonusaufgaben
- Zeige die IP-Adresse(n) mit den meisten Zugriffen an.
- Suche alle Zeilen, die einen Fehlercode (>= 400) enthalten, und speichere sie in einer separaten Datei `errors.log`.
- Erweitere das Skript, sodass der Benutzer den Namen des Logfiles eingeben kann.

## Hinweise
- Nutze Python-Datenstrukturen wie **Listen**, **Sets** und **Dictionaries**.
- Die Bearbeitung erfolgt zeilenweise.
