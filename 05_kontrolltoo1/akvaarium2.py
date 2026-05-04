
class Akvaarium:
    def __init__(self, capacity, fill):
        self.capacity=capacity
        self.fill=fill
        
    def addWater(self):
        if self.capacity > self.fill:
            userInput = int(input("Sisesta mitu liitrit vett soovid akvaariumisse lisada: "))
        else:
            print("Akvaarium on täis, ei saa rohkem vett lisada")
        if userInput + self.fill <= self.capacity:
            self.fill += userInput
            print("Akvaariumisse lisati", userInput, "liitrit vett.")
        else:
            print("Akvaariumisse ei saa nii palju vett lisada")
                     
    def askFill(self):
        return self.fill

akvaarium1 = Akvaarium(100,20)    
print(akvaarium1.askFill())
akvaarium1.addWater()
print(akvaarium1.askFill())