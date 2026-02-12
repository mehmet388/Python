class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def is_volwassen(self):
        return self.leeftijd >= 18


# Stap 2: drie student-objecten maken
s1 = Student("Ali", 19)
s2 = Student("Sara", 17)
s3 = Student("Jan", 18)

# Stap 3: studenten in een lijst zetten
studenten = [s1, s2, s3]

# Stap 4 + 5 + 6
aantal_volwassen = 0

for student in studenten:
    print(student.naam, student.leeftijd)

    if student.is_volwassen():
        print("Status: Volwassen")
        aantal_volwassen += 1
    else:
        print("Status: Minderjarig")

    print()  # lege regel voor nettere output

# Totaal printen
print("Aantal studenten van 18 jaar of ouder:", aantal_volwassen)
