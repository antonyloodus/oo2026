import random

class Koletis:
    def __init__(self, nimi, elu):
        self.nimi = nimi
        self.elu = elu

    def __str__(self):
        return f"{self.nimi} (elu: {self.elu})" if self.elu > 0 else f"{self.nimi} (langenud)"

class Kangelane:
    def __init__(self, nimi, joud):
        self.nimi = nimi
        self.joud = joud
        self.tapetud = 0

    def runda(self, koletis):
        if koletis.elu > 0:
            kahju = random.randint(1, self.joud)
            koletis.elu -= kahju
            print(f"{self.nimi} ründab koletist {koletis.nimi} (-{kahju} elu)")
            if koletis.elu <= 0:
                self.tapetud += 1
                print(f"  >>> {koletis.nimi} langes!")
        else:
            print(f"{self.nimi} ei rünnanud koletist {koletis.nimi} (juba langenud)")

    def __str__(self):
        return f"{self.nimi}: tappis {self.tapetud} koletist"

class Areen:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kangelased = []
        self.koletised = []

    def lisa_kangelane(self, kangelane):
        self.kangelased.append(kangelane)

    def lisa_koletis(self, koletis):
        self.koletised.append(koletis)

    def simuleeri_lahingut(self, voorud=5):
        for voor in range(voorud):
            print(f"Voor {voor + 1}:")
            kangelane = random.choice(self.kangelased)
            koletis = random.choice(self.koletised)
            kangelane.runda(koletis)
            print()

        print("Kangelased:")
        for kangelane in self.kangelased:
            print(kangelane)

        print("\nKoletised:")
        for koletis in self.koletised:
            print(koletis)

areen = Areen("Surmaorg")

areen.lisa_koletis(Koletis("Ork", 12))
areen.lisa_koletis(Koletis("Troll", 20))
areen.lisa_koletis(Koletis("Goblin", 8))

areen.lisa_kangelane(Kangelane("Aragorn", 8))
areen.lisa_kangelane(Kangelane("Legolas", 10))

areen.simuleeri_lahingut(8)