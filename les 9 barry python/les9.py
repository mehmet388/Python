# Functie om veilige integer input te krijgen
def vraag_int(prompt):
    while True:
        try:
            waarde = int(input(prompt))
            return waarde
        except ValueError:
            print("Ongeldige invoer, voer een getal in.")


# Functie om te delen met eigen fout
def delen(a, b):
    if b == 0:
        raise ZeroDivisionError("Delen door 0 mag niet")
    return a / b


# Menu loop
while True:
    print("\n--- MENU ---")
    print("1 = Optellen")
    print("2 = Delen")
    print("0 = Stoppen")

    try:
        keuze = vraag_int("Kies: ")

        if keuze == 0:
            print("Programma gestopt.")
            break

        elif keuze == 1:
            a = vraag_int("Getal 1: ")
            b = vraag_int("Getal 2: ")
            print("Uitkomst:", a + b)

        elif keuze == 2:
            a = vraag_int("Getal 1: ")
            b = vraag_int("Getal 2: ")
            resultaat = delen(a, b)
            print("Uitkomst:", resultaat)

        else:
            print("Ongeldige keuze.")

    except ZeroDivisionError as e:
        print("Fout:", e)

    finally:
        print("Terug naar menu...")