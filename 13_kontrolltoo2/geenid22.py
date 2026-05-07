import random

class Alleel:
    def __init__(self, nimetus, positiivne):
        self.nimetus = nimetus
        self.positiivne = positiivne

    def __str__(self):
        return f"{self.nimetus}({'+' if self.positiivne == 1 else '-'})"

class Geen:
    def __init__(self, alleel1: Alleel, alleel2: Alleel):
        if alleel1.nimetus != alleel2.nimetus:
            raise ValueError("Mõlema alleeli nimetus peab ühtima!")
        self.alleel1 = alleel1
        self.alleel2 = alleel2
        self.nimetus = alleel1.nimetus

    def onPositiivne(self):
        return self.alleel1.positiivne == 1 or self.alleel2.positiivne == 1

    def juhuslikAlleel(self):
        return random.choice([self.alleel1, self.alleel2])

    def __str__(self):
        tulemus = "Positiivne" if self.onPositiivne() else "Negatiivne"
        return f"{self.alleel1} | {self.alleel2} → {tulemus}"


def yhendaGeenid(vanem1: Geen, vanem2: Geen) -> Geen:
    return Geen(vanem1.juhuslikAlleel(), vanem2.juhuslikAlleel())

alleel11 = Alleel("reesus", 1)
alleel22 = Alleel("reesus", 0)
alleel33 = Alleel("test", 0)
alleel44 = Alleel("test", 1)
geen_reesus = Geen(alleel11, alleel22)
geen_test = Geen(alleel33, alleel44)

print("Juhuslik alleel:", geen_reesus.juhuslikAlleel())
print("Juhuslik alleel:", geen_test.juhuslikAlleel())

nimetus = input("Alleeli nimetus: ")

vanem1 = Geen(
    Alleel(nimetus, int(input("Vanem 1, alleel 1 (1=pos, 0=neg): "))),
    Alleel(nimetus, int(input("Vanem 1, alleel 2 (1=pos, 0=neg): ")))
)

vanem2 = Geen(
    Alleel(nimetus, int(input("Vanem 2, alleel 1 (1=pos, 0=neg): "))),
    Alleel(nimetus, int(input("Vanem 2, alleel 2 (1=pos, 0=neg): ")))
)

laps = yhendaGeenid(vanem1, vanem2)
print("\nLapse geen:", laps)

