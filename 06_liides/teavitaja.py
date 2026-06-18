from abc import ABC, abstractmethod

class Teavitaja(ABC):
    @abstractmethod
    def saada(self, sonum: str):
        pass

class Epost(Teavitaja):
    def __init__(self, aadress: str):
        self.aadress = aadress

    def saada(self, sonum: str):
        print(f"E-kiri saadetud aadressile {self.aadress}: \"{sonum}\"")

class SMS(Teavitaja):
    def __init__(self, number: str, krediit: int):
        self.number = number
        self.krediit = krediit

    def saada(self, sonum: str):
        if self.krediit >= 1:
            self.krediit -= 1
            print(f"SMS saadetud numbrile {self.number}: \"{sonum}\". Alles {self.krediit} krediiti.")
        else:
            print(f"Viga: numbril {self.number} pole enam SMS-krediiti!")

def teavita(meetod: Teavitaja, sonum: str):
    meetod.saada(sonum)

if __name__ == "__main__":
    print("TEAVITUSTE SAATMINE")

    # objektid
    tootaja = Epost("tootaja@ettevote.ee")
    klient = Epost("klient@klient.ee")
    valve = SMS("+37251234567", 2)

    # näidised
    teavita(tootaja, "Koosolek algab kell 14:00.")
    teavita(klient, "Teie tellimus on teel.")
    teavita(valve, "Häire käivitatud!")
    teavita(valve, "Süsteem taastatud.")
    teavita(valve, "Test")
