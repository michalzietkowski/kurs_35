import math

class FiguraGeometryczna:
    def oblicz_pole(self):
        return None

    def oblicz_obwod(self):
        return None


def oblicz_obwod_zaawansowanej_figury(figury: list[FiguraGeometryczna]):
    obwod_figury = 0
    for figura in figury:
        obwod_figury += figura.oblicz_obwod()
    return obwod_figury


def oblicz_pole_zaawansowanej_figury(figury: list[FiguraGeometryczna]):
    pole_figury = 0
    for figura in figury:
        pole_figury += figura.oblicz_pole()
    return pole_figury


class Trojkat(FiguraGeometryczna):
    def __init__(self, podstawa, wysokosc):
        self.podstawa = podstawa
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return 0.5 * self.podstawa * self.wysokosc

    def oblicz_obwod(self):
        return self.podstawa + 2 * ((self.podstawa / 2) ** 2 + self.wysokosc ** 2) ** 0.5


class Kwadrat(FiguraGeometryczna):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return self.bok ** 2

    def oblicz_obwod(self):
        return 4 * self.bok


class Okrag(FiguraGeometryczna):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return math.pi * self.promien ** 2

    def oblicz_obwod(self):
        return 2 * math.pi * self.promien


class Romb(FiguraGeometryczna):
    def __init__(self, bok, wysokosc):
        self.bok = bok
        self.wysokosc = wysokosc

    def oblicz_pole(self):
        return self.bok * self.wysokosc

    def oblicz_obwod(self):
        return 4 * self.bok


print(oblicz_obwod_zaawansowanej_figury([Trojkat(3, 4), Kwadrat(5), Okrag(2), Romb(3, 4)]))

print(oblicz_pole_zaawansowanej_figury([Trojkat(3, 4), Kwadrat(5), Okrag(2), Romb(3, 4)]))