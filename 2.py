class Xodim:
    def __init__(self, ism, maosh):
        self.ism = ism
        self.maosh = maosh

    def malumot(self):
        print(f"Ism: {self.ism}, maosh: {self.maosh}")


class Oqituvchi(Xodim):
    def __init__(self, ism, maosh, fan):
        super().__init__(ism, maosh)
        self.fan = fan

    def malumot(self):
        super().malumot()
        print(f"Fan: {self.fan}")


class Farrosh(Xodim):
    def __init__(self, ism, maosh, qavat):
        super().__init__(ism, maosh)
        self.qavat = qavat

    def malumot(self):
        super().malumot()
        print(f"Qavat: {self.qavat}")


o1 = Oqituvchi("Malika", 4000000, "Matematika")
f1 = Farrosh("Karim", 2000000, 2)
o1.malumot()
f1.malumot()