def aritKeskmine(a, b, c):
    return round((a + b + c) / 3, 2)

print(aritKeskmine(82, 4, 174))


def libisevArit(massiiv):
    keskmised = []
    for i in range(len(massiiv) - 2):
        keskmisedArvutus = round((massiiv[i] + massiiv[i + 1] + massiiv[i + 2]) / 3, 2)
        keskmised.append(keskmisedArvutus)
    return keskmised

print(libisevArit([17, 42, 342, 76, 38, 842, 7, 3, 869]))


class Libisev:
    def __init__(self, arvud):
        self.arvud = arvud
        self.keskmised = []
        for i in range(len(self.arvud) - 2):
            self.keskmised.append(round((self.arvud[i] + self.arvud[i + 1] + self.arvud[i + 2]) / 3, 2))

    def arvuLisaja(self, *lisamiseks):
        for arv in lisamiseks:
            self.arvud.append(arv)
            if len(self.arvud) >= 3:
                uus = round((self.arvud[-3] + self.arvud[-2] + self.arvud[-1]) / 3, 2)
                self.keskmised.append(uus)

    def libisevKeskmine(self):
        return self.keskmised


klass = Libisev([5, 2, 6])
print(klass.libisevKeskmine())
klass.arvuLisaja(8, 7, 4)
print(klass.libisevKeskmine())
klass.arvuLisaja(2)
print(klass.libisevKeskmine())