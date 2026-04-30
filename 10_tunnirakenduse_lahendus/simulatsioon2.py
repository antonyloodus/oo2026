#Lisa lahendusele võimalus vee välja valamiseks.
#Simuleeri olukord, kus kõigepealt täidetakse kann 1 liitri 20-kraadise veega. Seejärel kuumutatakse keemiseni. 
#Lastakse jahtuda 1 minut. Valatakse välja 400 ml vett. Lastakse jahtuda 3 minutit.

##Märgi kui kaua aega kulus keema minekuks, mitme kraadine oli vesi enne valamist ning mitme kraadine pärast teist jahtumist.
##Võrdle temperatuure olukorraga, kus pärast keema minekut lastakse jahtuda 4 minutit, vahepeal vett välja ei valata.

class SimulationExample:
    SPECIFIC_HEAT_CAPACITY = 4200
    JOULES_PER_KELVIN_SEC = 1.0 * 4200 * 2 / (100 * (100 - 20))

    def __init__(self, water_amount, temperature, heating_power, outside_temperature):
        if water_amount > 2000:
            raise RuntimeError("Vaid kaks liitrit mahub")
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

    def pour_out(self, milliliters):
        if milliliters > self.water_amount:
            raise RuntimeError("Nii palju vett pole kannus")
        self.water_amount -= milliliters

    def heat_until_boiling(self, step_seconds=1):
        total_time = 0
        while self.temperature < 100:
            self.heat(step_seconds)
            total_time += step_seconds
        return total_time


if __name__ == "__main__":
    w1 = SimulationExample(1000, 20, 1500, 20)
    boiling_time = w1.heat_until_boiling()
    print(f"Keema mineku aeg: {boiling_time} sekundit")

    for _ in range(60):
        w1.cool(1)
    print(f"Temperatuur enne valamist: {w1.get_temperature()}")

    w1.pour_out(400)

    for _ in range(180):
        w1.cool(1)
    print(f"Temperatuur pärast teist jahtumist: {w1.get_temperature()}")

    w2 = SimulationExample(1000, 20, 1500, 20)
    w2.heat_until_boiling()
    for _ in range(240):
        w2.cool(1)
    print(f"Võrdluseks (4 min jahtumist ilma valamiseta): {w2.get_temperature()}")