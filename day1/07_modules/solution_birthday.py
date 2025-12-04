from datetime import datetime, date, timedelta

# Eingabe des Geburtsdatums
geburtsdatum_str = input("Gib dein Geburtsdatum ein (TT.MM.JJJJ): ")
geburtsdatum = datetime.strptime(geburtsdatum_str, "%d.%m.%Y").date()

# Heutiges Datum
heute = date.today()

# Alter berechnen
alter = heute.year - geburtsdatum.year
if (heute.month, heute.day) < (geburtsdatum.month, geburtsdatum.day):
    alter -= 1

# Wochentag des Geburtsdatums
wochentag = geburtsdatum.strftime("%A")  # z.B. 'Monday'

# Tage bis zum nächsten Geburtstag
naechster_geburtstag = date(heute.year, geburtsdatum.month, geburtsdatum.day)
if naechster_geburtstag < heute:
    naechster_geburtstag = date(heute.year + 1, geburtsdatum.month, geburtsdatum.day)
tage_bis = (naechster_geburtstag - heute).days

# Ausgabe
print(f"Du bist {alter} Jahre alt.")
print(f"Du wurdest an einem {wochentag} geboren.")
print(f"Es sind noch {tage_bis} Tage bis zu deinem nächsten Geburtstag.")
