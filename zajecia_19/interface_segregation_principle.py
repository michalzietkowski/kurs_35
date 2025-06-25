from abc import ABC, abstractmethod
#
# class Zwierze(ABC):
#     @abstractmethod
#     def plywaj(self):
#         pass
#
#     @abstractmethod
#     def lataj(self):
#         pass
#
#     @abstractmethod
#     def biegaj(self):
#         pass
#
# class Kangur(Zwierze):
#     def plywaj(self):
#         raise NotImplementedError("Kangury nie pływają!")
#
#     def lataj(self):
#         raise NotImplementedError("Kangury nie latają!")
#
#     def biegaj(self):
#         return "Kangur skacze!"
#
# class Ryba(Zwierze):
#     def plywaj(self):
#         return "Ryba pływa!"
#
#     def lataj(self):
#         raise NotImplementedError("Ryby nie latają!")
#
#     def biegaj(self):
#         raise NotImplementedError("Ryby nie biegają!")
#

# class Zwierze(ABC):
#     @abstractmethod
#     def rozmnoz_sie(self):
#         pass
#
# class LatajaceZwierze(Zwierze):
#     @abstractmethod
#     def lataj(self):
#         pass
#
# class PlywajaceZwierze(Zwierze):
#     @abstractmethod
#     def plywaj(self):
#         pass
#
# class BiegajaceZwierze(Zwierze):
#     @abstractmethod
#     def biegaj(self):
#         pass
#
#
# class Kangur(BiegajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Kangur rozmnaża się!"
#
#     def biegaj(self):
#         return "Kangur skacze!"
#
#
# class Ryba(PlywajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Ryba składa jaja!"
#
#     def plywaj(self):
#         return "Ryba pływa!"
#
# class Orzel(LatajaceZwierze):
#     def rozmnoz_sie(self):
#         return "Orzeł składa jaja!"
#
#     def lataj(self):
#         return "Orzeł lata wysoko!"


class Plywajace(ABC):
    @abstractmethod
    def plywaj(self):
        pass

class Latajace(ABC):
    @abstractmethod
    def lataj(self):
        pass

class Biegajace(ABC):
    @abstractmethod
    def biegaj(self):
        pass

class Czlowiek(Biegajace, Plywajace):
    def biegaj(self):
        return "Człowiek biegnie!"

    def plywaj(self):
        return "Człowiek pływa!"

class Kaczka(Plywajace, Latajace):
    def lataj(self):
        return "Kaczka lata!"

    def plywaj(self):
        return "Kaczka pływa!"