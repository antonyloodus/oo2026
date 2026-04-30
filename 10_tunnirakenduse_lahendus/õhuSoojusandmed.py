#Loo materjalikoguse klassile alamklass õhu soojusandmete hoidmiseks. 
#Konstruktoris antakse parameetritena ette toa pikkus, laius ja kõrgus ning algtemperatuur. 
#Sarnaselt toimib käsklus energia lisamise kohta. 
#Õhu erisoojuseks tavatingimustel ligikaudu 1012 J/(Kg*K), tihedus ehk erikaal 1,23 kilogrammi kuupmeetri kohta. 
#Katseta eksemplari tööd 3x4x2,5 meetrise toa õhu soojendamisel 100000 džauli võrra.

class MaterialAmount:
    def __init__(self, mass, specific_heat_capacity, temperature):
        self.mass = mass
        self.specific_heat_capacity = specific_heat_capacity
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

    def change_energy(self, joules):
        self.temperature += joules / (self.specific_heat_capacity * self.mass)


class AirAmount(MaterialAmount):
    AIR_DENSITY = 1.23
    AIR_SPECIFIC_HEAT_CAPACITY = 1012

    def __init__(self, length, width, height, temperature):
        mass = length * width * height * self.AIR_DENSITY
        super().__init__(mass, self.AIR_SPECIFIC_HEAT_CAPACITY, temperature)


if __name__ == "__main__":
    room_air = AirAmount(3, 4, 2.5, 20)
    print(f"Algtemperatuur: {room_air.get_temperature()}")
    room_air.change_energy(100000)
    print(f"Pärast 100000 džauli lisamist: {room_air.get_temperature()}")