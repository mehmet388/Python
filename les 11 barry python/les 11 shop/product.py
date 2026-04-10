class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} - €{self.prijs} (voorraad: {self._voorraad})")

    def is_op_voorraad(self, aantal=1):
        return self._voorraad >= aantal

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            return False

        if self._voorraad >= aantal:
            self._voorraad -= aantal
            return True

        return False