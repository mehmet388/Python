class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self.voorraad = voorraad

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            return False

        if aantal > self.voorraad:
            return False

        self.voorraad -= aantal
        return True


class Winkelmandje:
    def __init__(self):
        self.items = []  # (product, aantal)

    def voeg_toe(self, product, aantal):
        if aantal <= 0:
            return False

        if aantal > product.voorraad:
            return False

        self.items.append((product, aantal))
        return True

    def totaal_prijs(self):
        totaal = 0

        for product, aantal in self.items:
            totaal += product.prijs * aantal

        return totaal