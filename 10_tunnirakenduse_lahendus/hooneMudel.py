#Koosta klass materjalikoguse tarbeks. Materjalikogusel on mass, erisoojus ja algtemperatuur. Küsida saab temperatuuri.
#Lisa käsklus energiavahetuseks - positiivse väärtusega parameeter lisab energiat, negatiivne eemaldab (soojus)energiat. 
#Endiselt saab küsida temperatuuri. Loo eksemplar ja katseta.

class MaterialAmount:
    def __init__(self, mass, specific_heat_capacity, temperature):
        self.mass = mass
        self.specific_heat_capacity = specific_heat_capacity
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def change_energy(self, joules):
        self.temperature += joules / (self.specific_heat_capacity * self.mass)


if __name__ == "__main__":
    water_pot = MaterialAmount(3, 4200, 20)
    water_pot.change_energy(10000)
    print(water_pot.get_temperature())

    iron_radiator = MaterialAmount(10, 412, 20)
    iron_radiator.change_energy(10000)
    print(iron_radiator.get_temperature())

    if iron_radiator.get_temperature() > water_pot.get_temperature():
        change_amount = 1000
        iron_radiator.change_energy(-change_amount)
        water_pot.change_energy(change_amount)

    print(water_pot.get_temperature(), iron_radiator.get_temperature())