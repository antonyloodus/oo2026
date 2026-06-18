import matplotlib.pyplot as plt

# graafilise väljundiga objekt
class Mull:
    def __init__(self, x, y, raadius, varv):
        self.x = x
        self.y = y
        self.raadius = raadius
        self.varv = varv

    def joonista(self, telg):
        ring = plt.Circle((self.x, self.y), self.raadius, color=self.varv, alpha=0.5)
        telg.add_patch(ring)

    def __str__(self):
        return f"{self.varv} mull keskpunktis ({self.x}, {self.y}), raadius {self.raadius}"

# haldusklass, mis tegeleb mullidega kordamööda
class Louend:
    def __init__(self, nimi):
        self.nimi = nimi
        self.mullid = []

    def lisa(self, mull):
        self.mullid.append(mull)

    def muuda_koiki(self):
        for mull in self.mullid:
            print(f"\nPraegune mull: {mull}")
            sisend = input("Uus keskpunkt (x y): ")
            x, y = sisend.split()
            mull.x = float(x)
            mull.y = float(y)
            mull.varv = input("Uus värv: ")
            print("Uuendatud:", mull)

    def kuva(self, oota=True):
        joonis, telg = plt.subplots()
        for mull in self.mullid:
            mull.joonista(telg)
        telg.set_aspect("equal")
        telg.set_xlim(0, 10)
        telg.set_ylim(0, 10)
        telg.grid(True)
        plt.title(self.nimi)
        plt.show(block=oota)
        plt.pause(0.1)

louend = Louend("Minu mullid")
louend.lisa(Mull(2, 3, 1, "red"))
louend.lisa(Mull(5, 5, 2, "blue"))

louend.kuva(oota=False)
louend.muuda_koiki()
louend.kuva()
