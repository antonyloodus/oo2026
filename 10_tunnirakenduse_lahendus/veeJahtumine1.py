#Koosta programm, millele antakse ette näitväärtused välistemperatuuri, kannu temperatuuri ning 30 sekundi jooksul muutunud kraadide kohta. 
#Programmilt saab küsida etteantud temperatuuril jahtutud kraadide arv 30 sekundi jooksul. 
#Testimiseks: kelder 10 kraadi, kann 20 kraadi, 30 sekundiga jahtus 0,1 kraadi. 
#60 kraadi pealt võiks jahtuda 30 sekundiga 0,5 kraadi.

class CoolingKettle:
    def __init__(self, outside_temperature, kettle_temperature, degrees_cooled_in_30_sec):
        self.outside_temperature = outside_temperature
        self.reference_difference = kettle_temperature - outside_temperature
        self.reference_cooling = degrees_cooled_in_30_sec

    def get_cooling_in_30_sec(self, current_temperature):
        current_difference = current_temperature - self.outside_temperature
        return self.reference_cooling * current_difference / self.reference_difference


if __name__ == "__main__":
    k = CoolingKettle(10, 20, 0.1)
    print(k.get_cooling_in_30_sec(20))
    print(k.get_cooling_in_30_sec(60))