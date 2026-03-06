class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} - €{self.prijs} (voorraad: {self._voorraad})")

    def is_op_voorraad(self):
        return self._voorraad > 0

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            print("Aantal moet groter dan 0 zijn.")
            return False

        if self._voorraad >= aantal:
            self._voorraad -= aantal
            return True
        else:
            print("Niet genoeg voorraad.")
            return False


class Winkelmandje:
    def __init__(self):
        self.items = []

    def voeg_toe(self, product):
        self.items.append(product)
        print(f"Toegevoegd: {product.naam}")

    def toon_mandje(self):
        if len(self.items) == 0:
            print("Mandje is leeg")
            return

        print("In je mandje:")
        for p in self.items:
            print(f"- {p.naam} (€{p.prijs})")

    def totaal_prijs(self):
        totaal = 0
        for p in self.items:
            totaal += p.prijs
        return totaal


# Startproducten
producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5),
]

mandje = Winkelmandje()


# Menu loop
while True:
    print("\n--- MENU ---")
    print("1 = Producten bekijken")
    print("2 = Product toevoegen")
    print("3 = Mandje bekijken")
    print("4 = Afrekenen")
    print("0 = Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        print("\nProducten:")
        for i, p in enumerate(producten):
            print(i, end=" - ")
            p.toon_info()

    elif keuze == "2":
        for i, p in enumerate(producten):
            print(i, end=" - ")
            p.toon_info()

        try:
            nummer = int(input("Kies productnummer: "))
            product = producten[nummer]

            if product.is_op_voorraad():
                mandje.voeg_toe(product)
            else:
                print("Product is niet op voorraad.")

        except:
            print("Ongeldig productnummer.")

    elif keuze == "3":
        mandje.toon_mandje()
        print("Totaal: €", mandje.totaal_prijs())

    elif keuze == "4":
        if len(mandje.items) == 0:
            print("Mandje is leeg.")
            continue

        gelukt = True

        for p in mandje.items:
            if not p.verlaag_voorraad(1):
                gelukt = False

        if gelukt:
            print("Bedankt voor je aankoop!")
            print("Totaal betaald: €", mandje.totaal_prijs())
            mandje.items = []

    elif keuze == "0":
        print("Programma gestopt.")
        break

    else:
        print("Ongeldige keuze.")
