class FilmKutubxonasi:
    def __init__(self, nom, filmlar=None):
        self.nom = nom
        if filmlar is None:
            filmlar = []
        self.filmlar = filmlar

    def __len__(self):
        return len(self.filmlar)

    def __getitem__(self, indeks):
        return self.filmlar[indeks]

    def __contains__(self, film):
        return film in self.filmlar


k1 = FilmKutubxonasi("Mening kutubxonam", ["Avatar", "Titanik", "Interstellar"])
k2 = FilmKutubxonasi("Bo'sh kutubxona")

print(len(k1))               # 3
print(k1[0])                 # Avatar
print("Titanik" in k1)       # True
print("Matritsa" in k1)      # False
print(len(k2))               # 0