
# 01_funktsioon
-mingi ülesande eraldamine
-andmed sisse ja andmed välja
-alati ei anta andmeid (math.random, time jne)

# 02_klass
-mudeli loomine, simuleerimine
-lihtsus vs kompleksus

@staticmethod:
-Ei kasuta self/cls. 
-Justkui funktsioon klassi sees, sellel puudub otsene ligipääs klassi või objekti andmetele.
-Peamiselt kasutatakse funktsioonideks, mis loogiliselt kuuluvad klassi juurde, kuid ei sõltu otseselt klassi või instantsi andmetest.

    class Person:
    def __init__(self, age):
        self.age = age

    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(20))
p = Person(16)
print(p.is_adult(p.age))

# 03_klassikomplekt
-Mitu klassi, üksteisega seotud
-Keerukama mudeli loomine

# 04_proovikt1
# 05_kontrolltöö1

# 06_liides
-ABC, abstractmethod
-

# 07_testid
-erinevate stsenaariumite testimine
-koodis vigade leidmine

# 08_alamklassid
-peamisel klassil on tütarklassid - saab rohkem detaile lisada

# 09_tunnirakenduse_lahendus
-typescript
-js on dünaamiline, ts on staatiline
-ts'il on oop jaoks rohkem võimalusi, mugavam ja parem

