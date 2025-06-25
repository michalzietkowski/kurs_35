from curses import wrapper

uzytkownicy = [
    {
        "imie": "Jan",
        "nazwisko": "Kowalski",
        "wiek": 30,
        "rola_w_firmie": "Programista"
    },
    {
        "imie": "Anna",
        "nazwisko": "Nowak",
        "wiek": 25,
        "rola_w_firmie": "Tester"
    },
    {
        "imie": "Piotr",
        "nazwisko": "Zielinski",
        "wiek": 35,
        "rola_w_firmie": "Menadżer"
    }
]


def logowanie(func):
    def wrapper(*args, **kwargs):
        print("Sprawdzamy czy użytkownik się zalogował...")
        print("Wyciaganie uzytkownika z bazy lub sprawdzenie sesji...")
        func(*args, **kwargs)
        print("Użytkownik zalogowany!")
    return wrapper



class Firma:
    def __init__(self, uzytkownicy):
        self.uzytkownicy = uzytkownicy
        self.urlopy = []
        self.godziny = []

    def zaloguj_uzytkownika(self, imie, nazwisko):
        for uzytkownik in self.uzytkownicy:
            if uzytkownik["imie"] == imie and uzytkownik["nazwisko"] == nazwisko:
                return uzytkownik
        return None



    @logowanie
    def dodaj_urlop(self, imie, nazwisko, data_rozpoczecia, data_zakonczenia):
        urlop = {
            "imie": imie,
            "nazwisko": nazwisko,
            "data_rozpoczecia": data_rozpoczecia,
            "data_zakonczenia": data_zakonczenia
        }
        self.urlopy.append(urlop)
        return f"Urlop dla {imie} {nazwisko} został dodany."

    @logowanie
    def dodaj_godziny(self, imie, nazwisko, godziny):
        godziny_record = {
            "imie": imie,
            "nazwisko": nazwisko,
            "godziny": godziny
        }
        self.godziny.append(godziny_record)
        return f"Godziny dla {imie} {nazwisko} zostały dodane."

    @logowanie
    def wyplac_pieniadze(self, imie, nazwisko, kwota):
        print("Wyplacanie pieniędzy...")
        return f"Wypłacono {kwota} zł dla {imie} {nazwisko}."

    @staticmethod
    def przywitaj_sie():
        return "Witaj w systemie zarządzania firmą!"

firma = Firma(uzytkownicy)

firma.wyplac_pieniadze("Jan", "Kowalski", 1000)




# def glupia_funkcja(*args, **kwargs):
#     print("To jest głupia funkcja!")
#     print(args)
#     print(kwargs)
#
#
#
# glupia_funkcja(1, True, "aaaa", imie="Jan", nazwisko="Kowalski")
