class Akvaarium:
    def __init__(self, x, y, z, capacity, fill):
        self.x = x
        self.y = y
        self.z = z
        self.capacity = capacity
        self.fill = fill

    def moveWater(self):
        kogus = int(input("Sisesta mitu liitrit vett soovid esimesest akvaariumist teise valada: "))

        if kogus > akvaarium1.fill:
            print("Esimeses akvaariumis pole nii palju vett võtta.")
        elif akvaarium2.fill + kogus > akvaarium2.capacity:
            print("Teises akvaariumis pole piisavalt ruumi.")
        else:
            akvaarium1.fill -= kogus
            akvaarium2.fill += kogus
            print(f"Valatud! Akvaarium 1: {akvaarium1.fill}L, Akvaarium 2: {akvaarium2.fill}L")

            vaba1 = (akvaarium1.capacity - akvaarium1.fill) * 1000 / (akvaarium1.x * akvaarium1.y)
            vaba2 = (akvaarium2.capacity - akvaarium2.fill) * 1000 / (akvaarium2.x * akvaarium2.y)

            if vaba1 < 2:
                print("Hoiatus: esimeses akvaariumis on vähem kui 2 cm vaba ruumi!")
            if vaba2 < 2:
                print("Hoiatus: teises akvaariumis on vähem kui 2 cm vaba ruumi!")


akvaarium1 = Akvaarium(60, 30, 40, 72, 60)
akvaarium2 = Akvaarium(60, 30, 40, 72, 50)

akvaarium1.moveWater()