class Transport:
    def harakatlanish(self):
        print("Transport harakatlanmoqda.")


class Mashina(Transport):
    def harakatlanish(self):
        print("Mashina yo'lda tez yuryapti.")


class Velosiped(Transport):
    def harakatlanish(self):
        print("Velosiped pedal aylantirib ketyapti.")


class Poyezd(Transport):
    def harakatlanish(self):
        print("Poyezd relslar ustida ketyapti.")


transportlar = [Mashina(), Velosiped(), Poyezd()]
for t in transportlar:
    t.harakatlanish()