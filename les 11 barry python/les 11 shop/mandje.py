from .product import Product


class Winkelmandje:
    def __init__(self):
        self.items = []  # (product, aantal)

    def voeg_toe(self, product, aantal):
        self.items.append((product, aantal))
        print(f"Toegevoegd: {product.naam} x{aantal}")

    def totaal_prijs(self):
        totaal = 0
        for product, aantal in self.items:
            totaal += product.prijs * aantal
        return totaal

    def toon(self):
        if not self.items:
            print("Mandje is leeg")
            return

        print("\nMandje:")
        for product, aantal in self.items:
            print(f"{product.naam} x{aantal} = €{product.prijs * aantal}")

        print("Totaal: €", self.totaal_prijs())