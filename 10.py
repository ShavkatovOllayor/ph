class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx


class Savat:
    def __init__(self, nom, mahsulotlar=None):
        self.nom = nom
        if mahsulotlar is None:
            mahsulotlar = []
        self.mahsulotlar = mahsulotlar

    def qosh(self, mahsulot):
        self.mahsulotlar.append(mahsulot)

    def __len__(self):
        return len(self.mahsulotlar)

    def __bool__(self):
        return len(self.mahsulotlar) > 0

    def umumiy_narx(self):
        return sum(m.narx for m in self.mahsulotlar)

    def __str__(self):
        return f"Savat '{self.nom}': {len(self)} ta mahsulot"


savat1 = Savat("Mening savatim")
savat1.qosh(Mahsulot("Non", 5000))
savat1.qosh(Mahsulot("Sut", 12000))
savat1.qosh(Mahsulot("Tuxum", 18000))

savat2 = Savat("Bo'sh savat")

print(savat1)
if savat1:
    print("Savat bo'sh emas.")
    print("Umumiy narx:", savat1.umumiy_narx())

if not savat2:
    print(savat2, "- bo'sh")