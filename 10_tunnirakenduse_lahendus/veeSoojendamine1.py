#Koosta klass vee soojendamise arvestamiseks. 
#Väljadeks vee kogus, algtemperatuur ja soojendamise võimsus. 
#Meetodiga (funktsiooniga) saab määrata, mitmeks sekundiks lülitatakse lülitatakse soojendus sisse. 
#Teise meetodiga saab küsida vee temperatuuri.

class Water2:
    SPECIFIC_HEAT_CAPACITY = 4200

    def __init__(self, water_amount, temperature):
        self.water_amount = water_amount
        self.temperature = temperature
        self.heating_power = 0

    def set_heating_power(self, new_power):
        self.heating_power = new_power

    def heat_a_second(self):
        joules = self.heating_power
        delta_temperature = joules / (self.SPECIFIC_HEAT_CAPACITY * self.water_amount / 1000)
        self.temperature += delta_temperature

    def get_temperature(self):
        return self.temperature


if __name__ == "__main__":
    w = Water2(800, 20)
    w.set_heating_power(1500)
    for _ in range(120):
        w.heat_a_second()
    print(w.get_temperature())