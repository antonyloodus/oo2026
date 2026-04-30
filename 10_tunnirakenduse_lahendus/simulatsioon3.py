#Koosta simulaator vee hoidmiseks soojas. Soojendaja töötab kuni temperatuur tõuseb 95 kraadini. 
#Edasi kann jahtub kuni 90 kraadini, siis lülitatakse soojendaja uuesti sisse. 
#Pane simulaator tööle ning näita, millise aja tagant lülitub kannu soojendaja sisse, kui kannus on 2 liitrit vett ja toatemperatuur on 20 Celsiuse kraadi. 
#Võrdle tulemust olukorraga, kus kannus on 1 liiter vett ning kann on õuetelgis Celsiuse kümne külmakraadi juures. 
#Kui pikalt kummalgi puhul kann kütab, mitu kilovatt-tundi elektrienergiat tunnis kulutab.

class WarmKeeper:
    SPECIFIC_HEAT_CAPACITY = 4200
    JOULES_PER_KELVIN_SEC = 1.0 * 4200 * 2 / (100 * (100 - 20))
    UPPER_LIMIT = 95
    LOWER_LIMIT = 90

    def __init__(self, water_amount, temperature, heating_power, outside_temperature):
        if water_amount > 2000:
            raise RuntimeError("Vaid kaks liitrit mahub")
        self.water_amount = water_amount
        self.temperature = temperature
        self.heating_power = heating_power
        self.outside_temperature = outside_temperature
        self.heating_on = False

    def heat(self, seconds):
        joules = self.heating_power * seconds
        delta_temperature = joules / (self.SPECIFIC_HEAT_CAPACITY * self.water_amount / 1000)
        self.temperature += delta_temperature

    def cool(self, seconds):
        joules = (self.temperature - self.outside_temperature) * self.JOULES_PER_KELVIN_SEC * seconds
        delta_temperature = joules / (self.SPECIFIC_HEAT_CAPACITY * self.water_amount / 1000)
        self.temperature -= delta_temperature

    def get_temperature(self):
        return self.temperature

    def simulate_one_hour(self):
        cycle_durations = []
        heating_durations = []
        total_heating_seconds = 0

        current_cycle_time = 0
        current_heating_time = 0
        time_since_last_start = 0

        for _ in range(3600):
            if self.heating_on:
                self.heat(1)
                current_heating_time += 1
                total_heating_seconds += 1
                if self.temperature >= self.UPPER_LIMIT:
                    self.heating_on = False
            else:
                self.cool(1)
                if self.temperature <= self.LOWER_LIMIT:
                    self.heating_on = True
                    if current_heating_time > 0:
                        cycle_durations.append(time_since_last_start)
                        heating_durations.append(current_heating_time)
                    time_since_last_start = 0
                    current_heating_time = 0
            time_since_last_start += 1

        kwh_per_hour = self.heating_power * total_heating_seconds / 1000 / 3600
        return cycle_durations, heating_durations, total_heating_seconds, kwh_per_hour


if __name__ == "__main__":
    w1 = WarmKeeper(2000, 95, 1500, 20)
    cycles1, heatings1, total1, kwh1 = w1.simulate_one_hour()
    print("2 liitrit vett, toatemperatuur 20 kraadi:")
    print(f"  Sisselülituste vahed (sek): {cycles1}")
    print(f"  Kütmise kestused (sek): {heatings1}")
    print(f"  Kokku kütmist tunnis: {total1} sek")
    print(f"  Energiakulu: {kwh1:.4f} kWh tunnis")

    w2 = WarmKeeper(1000, 95, 1500, -10)
    cycles2, heatings2, total2, kwh2 = w2.simulate_one_hour()
    print("\n1 liiter vett, õuetelgis -10 kraadi:")
    print(f"  Sisselülituste vahed (sek): {cycles2}")
    print(f"  Kütmise kestused (sek): {heatings2}")
    print(f"  Kokku kütmist tunnis: {total2} sek")
    print(f"  Energiakulu: {kwh2:.4f} kWh tunnis")