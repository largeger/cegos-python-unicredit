import random

# Zufällige Zahl zwischen 1 und 10 generieren
zufallszahl = random.randint(1, 10)

print("Willkommen zum Zahlen-Ratespiel!")
print("Ich habe mir eine Zahl zwischen 1 und 10 ausgedacht.")
print("Du hast 3 Versuche, sie zu erraten.")

# Spieler hat 3 Versuche
versuche = 3

while versuche > 0:
    tipp = int(input(f"\nVersuch {4 - versuche}: Gib deine Zahl ein: "))
    
    if tipp == zufallszahl:
        print("🎉 Glückwunsch! Du hast die Zahl erraten!")
        break
    else:
        if tipp < zufallszahl:
            print("Zu niedrig! Versuch es höher.")
        else:
            print("Zu hoch! Versuch es niedriger.")
    
    versuche -= 1

if versuche == 0 and tipp != zufallszahl:
    print(f"\nLeider verloren! Die richtige Zahl war {zufallszahl}.")
