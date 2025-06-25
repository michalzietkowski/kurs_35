from abc import ABC, abstractmethod

class Ptak:
    def lataj(self):
        return "Lecę!"

class Golab(Ptak):
    def lataj(self):
        return "Głęboko latam!"

class Sikorka(Ptak):
    def lataj(self):
        return "Szybko latam!"

class Strus(Ptak):
    def lataj(self):
        raise NotImplementedError("Strus nie lata!")


class Ptak(ABC):
    @abstractmethod
    def daj_glos(self):
        pass

class LatajacyPtak(Ptak):
    @abstractmethod
    def lataj(self):
        pass

class NielatajacyPtak(Ptak):
    @abstractmethod
    def biegaj(self):
        pass


class Golab(LatajacyPtak):
    def daj_glos(self):
        return "Głęboko głosuję!"

    def lataj(self):
        return "Głęboko latam!"

class Sikorka(LatajacyPtak):
    def daj_glos(self):
        return "Szybko głosuję!"

    def lataj(self):
        return "Szybko latam!"

class Strus(NielatajacyPtak):
    def daj_glos(self):
        return "Strus głosuje!"

    def biegaj(self):
        return "Biegam szybko!"