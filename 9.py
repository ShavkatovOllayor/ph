class Karta:
    def __init__(self, egasi, raqam_oxiri, balans):
        self.egasi = egasi
        self.raqam_oxiri = raqam_oxiri
        self.balans = balans

    def __str__(self):
        return f"{self.egasi}: {self.balans} so'm"

    def __gt__(self, other):
        return self.balans > other.balans

    def __lt__(self, other):
        return self.balans < other.balans


k1 = Karta("Malika", "2805", 1500000)
k2 = Karta("Sardor", "1234", 2300000)

print(k1)
print(k2)
if k1 > k2:
    print(f"{k1.egasi}da mablag' ko'proq.")
elif k1 < k2:
    print(f"{k2.egasi}da mablag' ko'proq.")
else:
    print("Balanslar teng.")