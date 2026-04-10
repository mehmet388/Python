from shop.product import Product
from shop.mandje import Winkelmandje


producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5),
]

mandje = Winkelmandje()


while True:
    print("\n--- MENU ---")
    print("1 = Toon producten")
    print("2 = Voeg toe")
    print("3 = Toon mandje")
    print("0 = Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        for i, p in enumerate(producten):
            print(i, end=" - ")
            p.toon_info()

    elif keuze == "2":
        for i, p in enumerate(producten):
            print(i, end=" - ")
            p.toon_info()

        try:
            index = int(input("Kies productnummer: "))
            aantal = int(input("Aantal: "))

            product = producten[index]

            if product.is_op_voorraad(aantal):
                if product.verlaag_voorraad(aantal):
                    mandje.voeg_toe(product, aantal)
                else:
                    print("Niet genoeg voorraad.")
            else:
                print("Niet genoeg voorraad.")

        except:
            print("Ongeldige invoer.")

    elif keuze == "3":
        mandje.toon()

    elif keuze == "0":
        print("Programma gestopt.")
        break

    else:
        print("Ongeldige keuze.")