class Inson:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh


class Talaba(Inson):
    def __init__(self, ism, yosh, universitet, baho):
        super().__init__(ism, yosh)
        self.universitet = universitet
        self.baho = baho

    def natija(self):
        if self.baho >= 86:
            return "A'lo"
        elif self.baho >= 71:
            return "Yaxshi"
        elif self.baho >= 56:
            return "Qoniqarli"
        else:
            return "Qoniqarsiz"


t1 = Talaba("Malika", 19, "TATU", 92)
t2 = Talaba("Sardor", 20, "TATU", 48)
for t in (t1, t2):
    print(f"{t.ism} ({t.universitet}): {t.baho} - {t.natija()}")