class Resistor:
    def __init__(self, r, max_power):
        self.r=r
        self.max_power=max_power

    def get_Current(self, u):
        return u / self.r
    
    def get_Power(self, u):
        return u * self.r
    
    def isVoltageAllowed(self, u):
        return self.get_Power(u) <= self.max_power

class ResistorRun1:
    @staticmethod
    def main():
        r1 = Resistor(50,120)
        print(r1.get_Current(5), r1.get_Power(5), r1.isVoltageAllowed(24))
        m=[r1, Resistor(500,100), Resistor(400,250), Resistor(30,500), Resistor(220,20)]
        for t in ResistorRun1.leiaSobivad(m,2):
            print(t.r, t.max_power)

    def leiaSobivad(takistid, u):
        return [t for t in takistid if t.isVoltageAllowed(u)]

if __name__ == "__main__":
    ResistorRun1.main()
    #ResistorRun1.leiaSobivad(10)
    