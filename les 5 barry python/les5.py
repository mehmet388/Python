class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self._leeftijd = leeftijd  # protected attribuut (conventie)

    # Getter
    def get_leeftijd(self):
        return self._leeftijd

    # Setter met validatie
    def set_leeftijd(self, nieuwe_leeftijd):
        if nieuwe_leeftijd < 0:
            print("Leeftijd mag niet negatief zijn!")
            return
        
        if nieuwe_leeftijd > 130:
            print("Leeftijd mag niet hoger zijn dan 130!")
            return
        
        self._leeftijd = nieuwe_leeftijd

    # Methode om 1 jaar ouder te worden
    def verjaar(self):
        huidige_leeftijd = self.get_leeftijd()
        nieuwe_leeftijd = huidige_leeftijd + 1
        self.set_leeftijd(nieuwe_leeftijd)


# ===== TEST CODE =====

s1 = Student("Ali", 19)

print("Startleeftijd:", s1.get_leeftijd())

s1.set_leeftijd(20)
print("Na wijziging:", s1.get_leeftijd())

s1.set_leeftijd(-5)   # Fout
print("Na foute invoer:", s1.get_leeftijd())

s1.set_leeftijd(150)  # Fout
print("Na te hoge invoer:", s1.get_leeftijd())

s1.verjaar()
print("Na verjaar():", s1.get_leeftijd())