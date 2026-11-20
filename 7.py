class Telefon:
    def __init__(self, brend, model, narx):
        self.brend = brend
        self.model = model
        self.narx = narx

    def __str__(self):
        narx = f"{self.narx:,}".replace(",", " ")
        return f"{self.brend} {self.model} — {narx} so'm"

    def __eq__(self, other):
        return self.narx == other.narx


t1 = Telefon("Samsung", "A54", 4500000)
t2 = Telefon("Xiaomi", "Redmi Note 12", 4500000)
t3 = Telefon("iPhone", "13", 8000000)

print(t1)
print(t2)
print(t1 == t2)   # True
print(t1 == t3)   # False