class Mitarbeiter:
    def __init__(self, name, position, gehalt):
        self.name = name
        self.position = position
        self.gehalt = gehalt

    def anzeigen(self):
        print(f"Mitarbeiter: {self.name}, Position: {self.position}, Gehalt: {self.gehalt}€")

    def gehalt_erhoehen(self, prozentsatz):
        self.gehalt += self.gehalt * (prozentsatz / 100)

# Beispielverwendung
m1 = Mitarbeiter("Lars", "Entwickler", 4000)
m1.anzeigen()
m1.gehalt_erhoehen(10)
m1.anzeigen()
