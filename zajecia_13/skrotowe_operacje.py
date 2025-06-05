########## Operacje(instrukcje) warunkowe

# wiek = int(input("Podaj wiek: "))
#
# if wiek >= 18:
#     pelnoletni = True
# else:
#     pelnoletni = False
#
# pelnoletni_skrot = True if wiek >= 18 else False
#
# # nazwa_zmiennej = <pierwsza_wartosc> if <warunek na pierwsza wartosc> else <druga_wartosc>
# print(pelnoletni)

############# List Comprehensions


lista_uczniow = ["Jan", "Anna", "Piotr", "kaSia", "marek"]

# poprawna_lista_uczniow = []
#
# for uczen in lista_uczniow:
#     poprawna_lista_uczniow.append(uczen.capitalize())

# print(poprawna_lista_uczniow)
#
# poprawna_lista_uczniow_comprehension = [uczen.capitalize() for uczen in lista_uczniow]
#
# print(poprawna_lista_uczniow_comprehension)
#
# # nazwa_zmiennej = [<wartosc, ktora zapisujemy w liscie> for <tymczasowa_zmienna> in <ITERABLE>]
#
# kwadraty_liczb = [x**2 for x in range(10)]
#
# print(kwadraty_liczb)


lista_dziewczynek = [uczen.capitalize() for uczen in lista_uczniow if uczen.lower().endswith("a")]
lista_chlopcow = [uczen.capitalize() for uczen in lista_uczniow if not uczen.lower().endswith("a")]
print(lista_dziewczynek)
print(lista_chlopcow)
# nazwa_zmiennej = [<wartosc, ktora zapisujemy w liscie> for <tymczasowa_zmienna> in <ITERABLE> if <warunek>]


####### Dict Comprehensions

slownik = {
    "imie": "Nazwisko",
}


lista_uczniow_nowa_struktura = [{
    "imie": "Jan",
    "nazwisko": "Kowalski",
    "wiek": 18
}, {
    "imie": "Anna",
    "nazwisko": "Nowak",
    "wiek": 17
}, {
    "imie": "Piotr",
    "nazwisko": "Zielinski",
    "wiek": 19
}]

# slownik_uczniow = {uczen: uczen.capitalize() for uczen in lista_uczniow}
#
# slownik_uczniow_1 = {index: value for index, value in enumerate(lista_uczniow) if value.lower().endswith("a")}
#
#
# print(slownik_uczniow_1)
# print(slownik_uczniow)

slownik_uczniow_nowa_struktura = {uczen["imie"]: uczen["nazwisko"] for uczen in lista_uczniow_nowa_struktura}
print(slownik_uczniow_nowa_struktura)