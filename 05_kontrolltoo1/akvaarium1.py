class Akvaarium:
    def __init__(self, pikkus, laius, korgus):
        self.pikkus=pikkus
        self.laius=laius
        self.korgus=korgus
    
    def leiaRuumala(self):
        if self.pikkus > 0 and self.laius > 0 and self.korgus > 0:
            ruumala = self.pikkus*self.laius*self.korgus
            return ruumala
        else: print("Akvaariumi mõõtmed on vigased")
        
akvaarium1 = Akvaarium(10, 5, 6)
print(akvaarium1.leiaRuumala())