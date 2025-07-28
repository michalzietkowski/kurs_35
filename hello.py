class Pilkarz:

    plec = "mezczyzna"

    def __init__(self, ilosc_lat, imie, nazwisko):
        self.ilosc_lat = ilosc_lat
        self.imie = imie
        self.nazwisko = nazwisko

    def zmien_nazwisko(self, nowe_nazwisko):
        self.nazwisko = nowe_nazwisko

    @classmethod
    def zmien_plec(cls, nowa_plec):
        cls.plec = nowa_plec

    @staticmethod
    def zaloguj_mi_wydarzenie(wydarzenie):
        print(f"zalogowalem wydarzenie {wydarzenie}")

czlowiek_1 = Pilkarz(20, "Michal", "Adamiec")
czlowiek_2 = Pilkarz(28, "Robert", "Lewandowski")

czlowiek_1.imie = "Andrzej"
print(czlowiek_1.imie)
print(czlowiek_2.imie)
print(czlowiek_2.plec)
print(czlowiek_2.plec)


Pilkarz.plec = "kobieta"
print(czlowiek_1.plec)
print(czlowiek_2.plec)
# czlowiek_1.zmien_nazwisko("Blaszczykowski")
# print(czlowiek_1.nazwisko)
# print(czlowiek_2.nazwisko)
czlowiek_1.zmien_plec("mezczyzna")
print(czlowiek_2.plec)
print(czlowiek_1.plec)

print(id(czlowiek_2.imie))
print(id(czlowiek_1.imie))
print(id(czlowiek_1.plec))
print(id(czlowiek_2.plec))

czlowiek_2.plec = "kobieta"

print(id(czlowiek_2.plec))
print(id(czlowiek_1.plec))

czlowiek_3 = Pilkarz(40, "Adam", "Malysz")
print(czlowiek_3.plec)

czlowiek_3.zmien_plec("obojniak")

print(czlowiek_3.plec)
print(czlowiek_1.plec)
print(czlowiek_2.plec)


print(id(czlowiek_2.zaloguj_mi_wydarzenie))
print(id(czlowiek_1.zaloguj_mi_wydarzenie))

nowa_nazwa_klasy = Pilkarz

czlowiek_4 = nowa_nazwa_klasy(20, "Artur", "Boruc")
print(czlowiek_4.plec)