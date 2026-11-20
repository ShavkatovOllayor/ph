class Kitob:
    def __init__(self, nom, muallif, sahifa_soni):
        self.nom = nom
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def malumot(self):
        print(f"Kitob: {self.nom}, muallif: {self.muallif}, sahifa: {self.sahifa_soni}")


class ElektronKitob(Kitob):
    def __init__(self, nom, muallif, sahifa_soni, format, fayl_hajmi):
        super().__init__(nom, muallif, sahifa_soni)
        self.format = format
        self.fayl_hajmi = fayl_hajmi

    def malumot(self):
        super().malumot()
        print(f"Format: {self.format}, hajmi: {self.fayl_hajmi} MB")


k1 = Kitob("O'tkan kunlar", "Abdulla Qodiriy", 400)
k2 = ElektronKitob("Mehrobdan chayon", "Abdulla Qodiriy", 350, "pdf", 5)
k1.malumot()
k2.malumot()