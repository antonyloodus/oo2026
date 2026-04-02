class Resistor:
    def __init__(self, r, max_power):
        self.r=r
        self.max_power=max_power

    def get_Current(self, u):
        return u / self.r
    
    def get_Power(self, u):
        return u * self.r
    
    def get_resistance(self):
        return self.r
    
    def isVoltageAllowed(self, u):
        return self.get_Power(u) <= self.max_power

class JadaYhendus:
    def __init__(self):
        self.tarbijad = []

    def lisaTarbija(self, r):
        self.tarbijad.append(r)

    def calculateResistance(self):
        total = 0
        for r in self.tarbijad:
            total += r.get_resistance()
        return total
    
    def get_current(self, u):
        return u / self.calculateResistance()
    
    def get_total_power():
        self.get_current

if __name__ == "__main__":
    jy = JadaYhendus()
    jy.lisaTarbija(Resistor(220,0.25))
    jy.lisaTarbija(Resistor(220,0.25))
    jy.lisaTarbija(Resistor(110,0.25))

    print(jy.calculateResistance())
    print(jy.get_current(12))
