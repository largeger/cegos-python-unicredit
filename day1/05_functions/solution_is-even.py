def ist_gerade(zahl):
    """
    Überprüft, ob eine Zahl gerade ist.
    
    Parameter:
    zahl (int): Die zu überprüfende Zahl
    
    Rückgabe:
    bool: True, wenn die Zahl gerade ist, False sonst
    """
    return zahl % 2 == 0

# Beispiele
print(ist_gerade(4))  # True
print(ist_gerade(7))  # False
