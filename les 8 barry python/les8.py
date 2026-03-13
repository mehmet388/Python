from abc import ABC, abstractmethod


# Abstracte class
class Betaalmethode(ABC):
    def __init__(self, naam):
        self.naam = naam

    @abstractmethod
    def betaal(self, bedrag):
        pass


# Subclass 1
class PinBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Pin")

    def betaal(self, bedrag):
        return f"Betaling van €{bedrag} gepind via {self.naam}."


# Subclass 2
class ContantBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Contant")

    def betaal(self, bedrag):
        return f"Betaling van €{bedrag} contant ontvangen."


# Subclass 3
class OnlineBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Online")

    def betaal(self, bedrag):
        return f"Online betaling van €{bedrag} succesvol verwerkt."


# Test met polymorfisme
methodes = [
    PinBetaling(),
    ContantBetaling(),
    OnlineBetaling()
]

for methode in methodes:
    print(methode.betaal(49.95))