totals = []

class Resistor:
    def __init__(self, r):
        self.r=r

    def get_current(self, u):
        return u / self.r

class ResistorRun1:
    @staticmethod
    def main():
        r1 = Resistor(110)
        r2 = Resistor(220)
        r3 = Resistor(4700)
        totals.append(r1.get_current(5))
        totals.append(r2.get_current(5))
        totals.append(r3.get_current(5))

if __name__ == "__main__":
    ResistorRun1.main()

total_sum = 0
for value in totals:
    total_sum += value
print("Sum:", total_sum)