class Zwierze:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print('Przedstawie sie')
        print("Witaj w zoo w Nowym Yorku!")
        return f"Jestem {self.imie}."

    def daj_glos(self):
        return "Zwierzę wydaje dźwięk."

class Lew(Zwierze):

    def przedstaw_sie(self):
        print("Jestem królem Dżungli!")
        return f"Jestem {self.imie}."

    def daj_glos(self):
        return "Roar!"


class Pies(Zwierze):

    def daj_glos(self):
        return "Hau hau!"


class Plywajace:
    def przedstaw_sie(self):
        return "Jestem zwierzęciem wodnym."


class Ryba(Plywajace):
    def __init__(self, imie, gatunek="ryba"):
        self.imie = imie
        self.gatunek = gatunek

    def plywaj(self):
        return "Pływam w wodzie."




class Rekin(Ryba, Zwierze):
    def __init__(self, imie, gatunek="rekin"):
        Zwierze.__init__(self, imie)
        Ryba.__init__(self, imie, gatunek)

# krol_lew = Lew("Simba")
# print(krol_lew.przedstaw_sie())

# pies_domowy = Pies("Burek")
# print(pies_domowy.przedstaw_sie())
#
# zlota_rybka = Ryba("Złotko")
# print(zlota_rybka.przedstaw_sie())

rekin_białorybi = Rekin("Rekin", "biały")

print(rekin_białorybi.przedstaw_sie())