class Product:
    def __init__(self, naam, prijs):
        self.naam = naam
        self.prijs = prijs


# Factory Pattern
class ProductFactory:

    @staticmethod
    def maak_product(soort):
        if soort == "laptop":
            return Product("Laptop", 899)

        elif soort == "muis":
            return Product("Muis", 25)

        elif soort == "toetsenbord":
            return Product("Toetsenbord", 59)

        else:
            raise ValueError("Onbekend producttype")


# Strategy Pattern
class GeenKorting:
    def pas_toe(self, totaal):
        return 0


class TienProcentBoven500:
    def pas_toe(self, totaal):
        if totaal > 500:
            return totaal * 0.10
        return 0


# Kassa
class Kassa:
    def __init__(self, korting_regel):
        self.producten = []
        self.korting_regel = korting_regel

    def voeg_toe(self, product):
        self.producten.append(product)

    def totaal(self):
        totaal = 0

        for product in self.producten:
            totaal += product.prijs

        return totaal

    def korting(self):
        return self.korting_regel.pas_toe(self.totaal())

    def eindbedrag(self):
        return self.totaal() - self.korting()


# Demo
factory = ProductFactory()

kassa = Kassa(TienProcentBoven500())

kassa.voeg_toe(factory.maak_product("laptop"))
kassa.voeg_toe(factory.maak_product("muis"))
kassa.voeg_toe(factory.maak_product("toetsenbord"))
kassa.voeg_toe(factory.maak_product("muis"))

print("Subtotaal: €", kassa.totaal())
print("Korting: €", kassa.korting())
print("Eindbedrag: €", kassa.eindbedrag())