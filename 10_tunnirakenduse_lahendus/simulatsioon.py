#Lisa klassile käsklus 100 sekundi jagu jahtumiseks. 
#Lisa käsklus kannu jahtumise simuleerimiseks 100 sekundi kaupa. 
#Leia kannu temperatuur 1000 sekundi möödudes. 
#Kuva temperatuur iga etapi järel.

class SimulationExample:
    SPECIFIC_HEAT_CAPACITY = 4200
    JOULES_PER_KELVIN_SEC = 1.0 * 4200 * 2 / (100 * (100 - 20))

    def __init__(self, water_amount, temperature, heating_power, outside_temperature):
        if water_amount > 2000:
            raise RuntimeError("Vett on üle 2 liitri!")
        self.water_amount = water_amount
        self.temperature = temperature
        self.heating_power = heating_power
        self.outside_temperature = outside_temperature

    def heat(self, seconds):
        joules = self.heating_power * seconds
        delta_temperature = joules / (self.SPECIFIC_HEAT_CAPACITY * self.water_amount / 1000)
        self.temperature += delta_temperature

    def get_temperature(self):
        return self.temperature

    def cool(self, seconds):
        joules = (self.temperature - self.outside_temperature) * self.JOULES_PER_KELVIN_SEC * seconds
        delta_temperature = joules / (self.SPECIFIC_HEAT_CAPACITY * self.water_amount / 1000)
        self.temperature -= delta_temperature

if __name__ == "__main__":
    w1 = SimulationExample(1000, 100, 1500, 20)
    w1.cool(100)
    print(w1.get_temperature())
    for _ in range(9):
        w1.cool(100)
        print(w1.get_temperature())

    w2 = SimulationExample(1000, 100, 1500, 20)
    w2.cool(1000)
    print("Teine, 1000 sekundit korraga:", w2.get_temperature())