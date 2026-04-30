#Koosta alamprogramm, kuhu antakse kahe veehulga kogus ja temperatuur, väljastatakse ühine lõpptemperatuur

def get_water_mix_temperature(amount1, temperature1, amount2, temperature2):
    return (amount1 * temperature1 + amount2 * temperature2) / (amount1 + amount2)

if __name__ == "__main__":
    print(get_water_mix_temperature(200, 40, 20, 95))