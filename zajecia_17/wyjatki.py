lista_uczniow = [{
        "imie": "Jan",
        "wiek": 20,
    }, {
        "imie": "Anna",
        "wiek": 22,
    }, {
        "imie": "Piotr",
        "wiek": 19,
    }]

try:
    wiek = int(input("Podaj wiek ucznia: "))
    numer_na_liscie = int(input("Podaj numer ucznia: "))

    uczen = lista_uczniow[numer_na_liscie] if lista_uczniow[numer_na_liscie].get("wiek") == wiek else None
# except ValueError as e:
#     print("Podano nieprawidłową wartość (wartość powinna być liczbowa):", e)
# except IndexError as e:
#     print("Podano nieprawidłowy numer ucznia (indeks poza zakresem listy):", e)
except (ValueError, IndexError) as e:
    print("Wystąpił błąd:", e)
finally:
    print("Koniec programu.")
