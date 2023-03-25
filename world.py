"""
Modul world reprezentuje svět a obsahuje definice tříd prostorů, předmětů (h-objektů) a batohu.
"""
print(f"===== Modul {__name__} ===== START")


####################################################################################
class Item:
    """
    Instance reprezentující h-objekty v prostorech hry a batohu.
    """

    def __init__(self, name: str):
        """Vytvoří objekt se zadaným názvem."""
        self.name = name


####################################################################################

class Place:
    """Instance reprezentující prostory hry."""

    def __init__(self, name: str):
        """Vytvoří prostor se zadaným názvem."""
        self.name = name


####################################################################################

class Bag:
    """Instance třídy reprezentuje batoh. """
    CAPACITY = 0  # maximální kapacita batohu


####################################################################################

# Aktuální prostor = prostor kde se nachází hráč
current_place = None

# Jediná instance batohu
BAG = Bag()

####################################################################################
print(f"===== Modul {__name__} ===== STOP")
