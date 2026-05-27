import json
from pathlib import Path
from dataclasses import dataclass


# Taak class
@dataclass
class Taak:
    titel: str
    klaar: bool = False

    def markeer_klaar(self):
        self.klaar = True

    def to_dict(self):
        return {
            "titel": self.titel,
            "klaar": self.klaar
        }

    @staticmethod
    def from_dict(data):
        return Taak(
            data["titel"],
            data["klaar"]
        )


# Takenlijst class
class Takenlijst:
    def __init__(self):
        self.taken = []
        self.filename = "taken.json"

    def voeg_toe(self, titel):
        if titel.strip() == "":
            print("Titel mag niet leeg zijn.")
            return

        taak = Taak(titel)
        self.taken.append(taak)
        print("Taak toegevoegd.")

    def toon(self):
        if not self.taken:
            print("Geen taken.")
            return

        print("\nTaken:")
        for i, taak in enumerate(self.taken, start=1):
            status = "✅" if taak.klaar else "⬜"
            print(f"{i}. {status} {taak.titel}")

    def markeer_klaar(self, index):
        if 0 <= index < len(self.taken):
            self.taken[index].markeer_klaar()
            print("Taak gemarkeerd als klaar.")
        else:
            print("Ongeldig taaknummer.")

    def verwijder(self, index):
        if 0 <= index < len(self.taken):
            verwijderde_taak = self.taken.pop(index)
            print(f"Verwijderd: {verwijderde_taak.titel}")
        else:
            print("Ongeldig taaknummer.")

    def save(self):
        data = [taak.to_dict() for taak in self.taken]

        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        if not Path(self.filename).exists():
            return

        with open(self.filename) as f:
            data = json.load(f)

        self.taken = [Taak.from_dict(d) for d in data]


# Programma starten
takenlijst = Takenlijst()
takenlijst.load()


# Menu loop
while True:
    print("\n--- TAKENPLANNER ---")
    print("1 = Toon taken")
    print("2 = Voeg taak toe")
    print("3 = Markeer taak als klaar")
    print("4 = Verwijder taak")
    print("0 = Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        takenlijst.toon()

    elif keuze == "2":
        titel = input("Titel van taak: ")
        takenlijst.voeg_toe(titel)

    elif keuze == "3":
        takenlijst.toon()

        try:
            nummer = int(input("Welk taaknummer is klaar? "))
            takenlijst.markeer_klaar(nummer - 1)

        except ValueError:
            print("Voer een geldig nummer in.")

    elif keuze == "4":
        takenlijst.toon()

        try:
            nummer = int(input("Welk taaknummer wil je verwijderen? "))
            takenlijst.verwijder(nummer - 1)

        except ValueError:
            print("Voer een geldig nummer in.")

    elif keuze == "0":
        takenlijst.save()
        print("Taken opgeslagen. Programma gestopt.")
        break

    else:
        print("Ongeldige keuze.")