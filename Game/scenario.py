print(f"===== Modul {__name__} ===== START")

_single_line = 30 * "-"
_double_line = 60 * "="


class Step:
    """
    Krok scénáře  definuje zadávaný příkaz a stav hry po jeho zpracování. Pomocí sekvence kroků tvořících scénář lze otestovat funkcionalitu hry.
    """
    # Atribut třídy pamatující si index naposledy vytvářeného kroku
    last_index: int = -1

    def __init__(self, command: str, message: str,
                 # Stav hry po provedení příkazu
                 place: str, neighbors: tuple[str], items: tuple[str], bag: tuple[str]):
        """

        :param command: zadaný příkaz
        :param message: Zpráva hry vypsaná v reakci na příkaz
        :param place:   aktuální prostor
        :param neighbors: Sousedé aktuálního prostoru
        :param items: H-objekty v aktuálním prostoru
        :param bag: H-objekty v batuhu
        """
        self.command = command
        self.message = message
        self.place = place
        self.neighbors = neighbors
        self.items = items
        self.bag = bag
        Step.last_index = Step.last_index + 1
        self.index = Step.last_index

    def __str__(self):
        """ Vrátí uživatelský popis instance. """
        return (f"{self.index}. \n"
                f"{self.command}\n{_single_line}\n"
                f"{self.message}\n{_single_line}\n"
                f"Aktuální prostor: {self.place}\n"
                f"Sousedé prostoru: {self.neighbors}\n"
                f"Předměty v prostoru: {self.items}\n"
                f"Předměty v batohu:   {self.bag}\n"
                f"{_double_line}")


############################################################################
def simulate_simple():
    for step in _HAPPY_SCENARIO:
        print(f"{step.index}. {step.command}\n{_single_line}\n"
              f"{step.message}\n{_double_line}")


def simulate_with_state():
    for step in _HAPPY_SCENARIO:
        print(step)
    print("Konec hry.")


############################################################################

# Základní úspěšný scénář demonstrující průběh hry,
# v něm hráč nezadává žádné chybné příkazy
# a směřuje co nejkratší cestou k zadanému cíli.
_HAPPY_SCENARIO = (
    Step('',
         'Vítejte!\n'
         'Toto je příběh o Červené Karkulce, babičce a vlkovi.\n'
         'Svými příkazy řídíte Karkulku, aby donesla věci babičce.\n'
         'Nebudete-li si vědět rady, zadejte znak ?.',
         'Domeček',
         ('Les',),
         ('Bábovka', 'Víno', 'Stůl', 'Panenka',),
         (),
         ),
    Step('Vezmi víno',
         'Karkulka dala do košíku objekt: Víno',
         'Domeček',
         ('Les',),
         ('Bábovka', 'Stůl', 'Panenka',),
         ('Víno',),
         ),
    Step('Vezmi bábovka',
         'Karkulka dala do košíku objekt: Bábovka',
         'Domeček',
         ('Les',),
         ('Stůl', 'Panenka',),
         ('Bábovka', 'Víno',),
         ),
    Step('Jdi LES',
         'Karkulka se přesunula do prostoru:\n'
         'Les s jahodami, malinami a pramenem vody',
         'Les',
         ('Domeček', 'Temný_les',),
         ('Maliny', 'Jahody', 'Studánka',),
         ('Bábovka', 'Víno',),
         ),
    Step('Jdi temný_les',
         'Karkulka se přesunula do prostoru:\n'
         'Temný_les s jeskyní a číhajícím vlkem',
         'Temný_les',
         ('Les', 'Jeskyně', 'Chaloupka',),
         ('Vlk',),
         ('Bábovka', 'Víno',),
         ),
    Step('Jdi chaloupka',
         'Karkulka se přesunula do prostoru:\n'
         'Chaloupka, kde bydlí babička',
         'Chaloupka',
         ('Temný_les',),
         ('Postel', 'Stůl', 'Babička',),
         ('Bábovka', 'Víno',),
         ),
    Step('Polož bábovka',
         'Karkulka vyndala z košíku objekt: Bábovka',
         'Chaloupka',
         ('Temný_les',),
         ('Postel', 'Stůl', 'Babička', 'Bábovka',),
         ('Víno',),
         ),
    Step('Polož VÍNO',
         'Karkulka vyndala z košíku objekt: Víno',
         'Chaloupka',
         ('Temný_les',),
         ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno',),
         (),
         ),
    Step('Konec',
         'Ukončili jste hru.\nDěkujeme, že jste si zahráli.',
         'Chaloupka',
         ('Temný_les',),
         ('Postel', 'Stůl', 'Babička', 'Bábovka', 'Víno',),
         (),
         ),
)

simulate_with_state()
############################################################################
print(f'===== Modul {__name__} ===== STOP')
