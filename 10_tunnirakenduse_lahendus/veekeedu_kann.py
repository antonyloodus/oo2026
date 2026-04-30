#Koosta programm, kus sisendiks on kannu võimsus, sees oleva vee hulk ja algtemperatuur. Väljundiks on vee keemaminekuks kulunud aeg.

WATER_DENSITY = 1
SPECIFIC_HEAT_CAPACITY = 4200

power_watts = float(input("Veekannu võimsus vattides: "))
water_ml = float(input("Mitu milliliitrit vett: "))
starting_temperature = float(input("Vee algtemperatuur Celsiuse kraadides: "))

joules_per_kelvin = SPECIFIC_HEAT_CAPACITY * WATER_DENSITY * water_ml / 1000
joules_needed = joules_per_kelvin * (100 - starting_temperature)
heating_time_sec = joules_needed / power_watts

print(f"Keema mineku aeg sekundites: {heating_time_sec}")
