class Alleel:
    def __init__(self, nimetus: str, positiivne: bool):
        self.nimetus=nimetus
        self.positiivne=positiivne

class Geen:
    def __init__(self, alleel1: Alleel, alleel2: Alleel):
        if alleel1.nimetus != alleel2.nimetus:
            raise ValueError("Mõlema alleeli nimetus peab ühtima!")
        self.alleel1 = alleel1
        self.alleel2 = alleel2
        self.nimetus = alleel1.nimetus

    def on_positiivne(self) -> bool:
        return self.alleel1.positiivne or self.alleel2.positiivne
     
alleel11 = Alleel("reesus", 1)
alleel22 = Alleel("reesus", 0)
alleel33 = Alleel("geen2", 1)
alleel44 = Alleel("geen2", 0)