#Kasuta eelnevas näites toodud materjalikoguse klassi. 
#Koosta alamprogramm, millele antakse ette kaks materjalikogust oma massi, erisoojuse ja temperatuuriga. 
#Tagastatakse tekkinud süsteemi ühtne lõpptemperatuur. Vajadusel lisa täiendavaid abifunktsioone. 
#Kontrolli kahe veekoguse puhul, et lõpptulemus oleks sama kui eelmises ülesandes. 
#Katseta vee ja rauaga, vee ja õhuga, vee raua ja õhuga.

class MaterialAmount:
    def __init__(self, mass, specific_heat_capacity, temperature):
        self.mass = mass
        self.specific_heat_capacity = specific_heat_capacity
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def get_joules_per_kelvin(self):
        return self.mass * self.specific_heat_capacity

    def change_energy(self, joules):
        self.temperature += joules / (self.specific_heat_capacity * self.mass)


class AirAmount(MaterialAmount):
    AIR_DENSITY = 1.23
    AIR_SPECIFIC_HEAT_CAPACITY = 1012

    def __init__(self, length, width, height, temperature):
        mass = length * width * height * self.AIR_DENSITY
        super().__init__(mass, self.AIR_SPECIFIC_HEAT_CAPACITY, temperature)


def get_equal_temperature(materials):
    joule_kelvin_sum = 0
    joule_sum = 0
    for m in materials:
        joule_kelvin_sum += m.get_joules_per_kelvin()
        joule_sum += m.get_joules_per_kelvin() * m.get_temperature()
    return joule_sum / joule_kelvin_sum


if __name__ == "__main__":
    water1 = MaterialAmount(0.2, 4200, 40)
    water2 = MaterialAmount(0.02, 4200, 95)
    print("Kaks veekogust:", get_equal_temperature([water1, water2]))

    water = MaterialAmount(3, 4200, 21)
    iron = MaterialAmount(10, 412, 55)
    print("Vesi ja raud:", get_equal_temperature([water, iron]))

    water_b = MaterialAmount(3, 4200, 21)
    air = AirAmount(3, 2, 2.5, 20)
    print("Vesi ja õhk:", get_equal_temperature([water_b, air]))

    water_c = MaterialAmount(3, 4200, 21)
    iron_c = MaterialAmount(10, 412, 55)
    air_c = AirAmount(3, 2, 2.5, 20)
    print("Vesi, raud ja õhk:", get_equal_temperature([water_c, iron_c, air_c]))