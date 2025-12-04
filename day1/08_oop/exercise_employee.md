# Übung: Klasse `Mitarbeiter` 

Erstelle eine Python-Klasse `Mitarbeiter` mit den folgenden Anforderungen:

## Attribute
- `name` (string)
- `position` (string)
- `gehalt` (float)

## Methoden
- `anzeigen()`: Gibt alle Informationen des Mitarbeiters in folgendem Format aus:  
  `"Mitarbeiter: {name}, Position: {position}, Gehalt: {gehalt}€"`

## Zusatzaufgabe (optional)
- Füge eine Methode `gehalt_erhoehen(prozentsatz)` hinzu, die das Gehalt um einen angegebenen Prozentsatz erhöht.

## Beispiel
```python
m1 = Mitarbeiter("Lars", "Entwickler", 4000)
m1.anzeigen()
m1.gehalt_erhoehen(10)
m1.anzeigen()
```