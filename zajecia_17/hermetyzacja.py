class Zolnierz:
    def __init__(self, imie, stopien, rodzaj_broni, dywizja):
        self.imie = imie
        self.stopien = stopien
        self.rodzaj_broni = rodzaj_broni
        self.__dywizja = dywizja
        self._nazwisko = "Nieznane"

    def set_dywizja(self, nowa_dywizja):
        self.__dywizja = nowa_dywizja

    def get_dywizja(self):
        return self.__dywizja


szeregowy = Zolnierz("Jan", "Szeregowy", "Karabin", "1 Dywizja Piechoty")
major = Zolnierz("Anna", "Major", "Pistolet", "2 Dywizja Zmechanizowana")


print(szeregowy.rodzaj_broni)

szeregowy.rodzaj_broni = "Karabin maszynowy"

print(szeregowy.rodzaj_broni)

szeregowy.set_dywizja("3 Dywizja Pancerna")

szeregowy.__dywizja = "4 Dywizja Powietrzna"

print(szeregowy.__dywizja)