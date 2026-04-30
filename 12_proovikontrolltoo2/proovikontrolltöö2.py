class Jook:
    def __init__(self, nimetus, liitriOH, tihedus):
        self.nimetus = nimetus
        self.liitriOH = liitriOH
        self.tihedus = tihedus
        
class Joogipudel:
    def __init__(self, maht, pudelityyp, mass, taarahind):
        self.maht = maht
        self.pudelityyp = pudelityyp
        self.mass = mass
        self.taarahind = taarahind
        self.jook = None

    def leiaMass(self):
        mass_kokku = 0
        if self.jook == None:
            mass_kokku = self.mass
        else:
            mass_kokku = (self.jook.tihedus*self.maht)+self.mass
        return mass_kokku

    def leiaPudeliOH(self):
        hind_kokku = 0
        if self.jook == None:
            hind_kokku = self.taarahind
        else:
            hind_kokku = (self.maht*self.jook.liitriOH)+self.taarahind
        return hind_kokku



class Joogivaat:
    def __init__(self, ruumala, t2ituvus):
        self.ruumala = ruumala
        self.t2ituvus = t2ituvus

    def t2idaPudel(self):




class JoogipudeliteKast:
    def __init__(self, tyyp, hind, mass, pesad):
        self.tyyp=tyyp
        self.hind=hind
        self.mass=mass
        self.pesad=pesad

    def leiaBrutoMass(self):
        brutomass = self.mass + (self.joogipudel.mass*self.pesad)
        return brutomass
    
    def leiaKastiOH(self):
        