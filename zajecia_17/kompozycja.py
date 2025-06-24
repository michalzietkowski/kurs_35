class Silnik:
    def __init__(self, moc):
        self.moc = moc

    def __str__(self):
        return f"Silnik o mocy {self.moc} KM"

    def uruchom_silnik(self):
        return "Silnik uruchomiony."

    def podnies_obroty(self):
        return "Obroty silnika podniesione."

class Felga:
    def __init__(self, rozmiar):
        self.rozmiar = rozmiar

    def __str__(self):
        return f"Felga o rozmiarze {self.rozmiar} cali"




class Samochod:
    def __init__(self, marka, model, silnik: Silnik, felga: Felga = None):
        self.marka = marka
        self.model = model
        self.silnik = silnik
        self.felga = felga

    def __str__(self):
        return f"{self.marka} {self.model}"

    def przetestuj_brzmienie_silnika(self):
        print(self.silnik.uruchom_silnik())
        print(self.silnik.podnies_obroty())


samochod = Samochod("Toyota", "Corolla", Silnik(150))
samochod_2 = Samochod("Ford", "Focus", Silnik(180))

samochod.przetestuj_brzmienie_silnika()

samochod_2.przetestuj_brzmienie_silnika()


felga_shimano = Felga(18)

felga_audi = Felga(19)

felga_hyundai = Felga(17)


samochod = Samochod("Toyota", "Corolla", Silnik(150), felga_shimano)
