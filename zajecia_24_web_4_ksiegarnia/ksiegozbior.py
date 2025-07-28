
from file_handler import file_handler, save_temporary_data

# bedziemy dzialali w jednej petli while True:
# lista ksiazek
# while True:
#     print("Wybierz jedną z poniższych opcji(Podaj numer):")
#     komenda = input("""
#         1. doładowanie
#         2. wypożycz
#         3. zakup
#         4. bieżący_stan
#         5. zestawienie
#         6. szczegóły_książki
#         7. dziennik
#         8. zakończ
#     """)
#     match komenda:
#         case "1":
#             kwota = float(input("Podaj kwotę o jaką chcesz zmienić saldo: "))
#             if saldo + kwota < 0:
#                 print("Nie możesz ustawić salda na wartość ujemną.")
#             else:
#                 saldo += kwota
#             print(saldo)
#             save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#         case "2":
#             isbn = input("Podaj numer ISBN książki do wypożyczenia: ")
#             ksiazka_znaleziona = False
#             for ksiazka in lista_ksiazek:
#                 if ksiazka.get("ISBN") == isbn:
#                     ksiazka_znaleziona = True
#                     if ksiazka["ilosc_na_stanie"] <= 0:
#                         print("Nie ma tej książki na stanie.")
#                         break
#                     ksiazka["ilosc_na_stanie"] -= 1
#                     saldo += 10  # koszt wypożyczenia książki
#                     historia.append(
#                         f"Wypożyczenie książki: {ksiazka['tytul']}, {ksiazka['autor']}, 1 sztuka"
#                     )
#                     save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#                     break
#             if not ksiazka_znaleziona:
#                 print("Taka książka nie istnieje.")
#         case "3":
#             tytul = input("Podaj tytuł książki: ")
#             autor = input("Podaj autora książki: ")
#             koszt = float(input("Podaj koszt zakupu książki: "))
#             ilosc = int(input("Podaj ilość egzemplarzy: "))
#             kategoria = input("Podaj kategorie książki: ")
#             numer_isbn = input("Podaj numer ISBN książki: ")
#             rok_wydania = int(input("Podaj rok wydania książki: "))
#             if saldo - (koszt * ilosc) < 0:
#                 print("Nie możesz ustawić salda na wartość ujemną.")
#                 historia.append(
#                     f"Próba zakupu książki: {tytul}, {koszt}, {ilosc} sztuk - nieudana"
#                 )
#                 continue
#             else:
#                 saldo -= koszt * ilosc
#             znaleziono_ksiazke = False
#             for ksiazka in lista_ksiazek:
#                 if ksiazka.get("ISBN") == numer_isbn:
#                     znaleziono_ksiazke = True
#                     ksiazka["ilosc_na_stanie"] += ilosc
#                     break
#             if not znaleziono_ksiazke:
#                 lista_ksiazek.append(
#                     {
#                         "tytul": tytul,
#                         "autor": autor,
#                         "cena": koszt,
#                         "ilosc_na_stanie": ilosc,
#                         "ilosc": ilosc,
#                         "kategoria": kategoria,
#                         "ISBN": numer_isbn,
#                         "rok_wydania": rok_wydania,
#                     }
#                 )
#                 historia.append(f"Zakup książki: {tytul}, {koszt}, {ilosc} sztuk")
#                 save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
#         case "5":
#             print(f"Zestawienie księgozbioru:{lista_ksiazek}")
#         case "7":
#             od = input("Podaj wartość 'od' (numer transakcji): ")
#             do = input("Podaj wartość 'do' (numer transakcji): ")
#             if od:
#                 od = int(od)
#             else:
#                 od = 0
#             if do:
#                 do = int(do)
#             else:
#                 do = len(historia)
#             print(historia[od:do])
#         case "8":
#             print("Zakończono działanie programu.")
#             break

# file_handler.ksiegozbior = lista_ksiazek
# file_handler.saldo = saldo
# file_handler.historia = historia
# file_handler.save_ksiegozbior_file()
# file_handler.save_saldo_file()
# file_handler.save_historia_file()

def get_books():
    """Returns the list of books in the collection."""
    return file_handler.ksiegozbior

def get_bookstore_state():
    """Returns the current state of the bookstore, including balance and history."""
    return {
        "saldo": file_handler.saldo,
        "historia": file_handler.historia,
        "ksiegozbior": get_books(),
    }


def create_new_book(book_form: dict):
    new_book = {
        "tytul": book_form.get("title"),
        "autor": book_form.get("author"),
        "cena": float(book_form.get("price", 0)),
        "ilosc_na_stanie": int(book_form.get("quantity", 0)),
        "ilosc": int(book_form.get("quantity", 0)),
        "kategoria": book_form.get("category"),
        "ISBN": book_form.get("isbn"),
        "rok_wydania": int(book_form.get("year", 0)),
    }
    file_handler.ksiegozbior.append(new_book)
    save_temporary_data(file_handler, file_handler.ksiegozbior, file_handler.saldo, file_handler.historia)
    pass

def update_book(isbn: str, book_form: dict):
    """Updates the book with the given ISBN using the provided book form."""
    # for book in lista_ksiazek:
    #     if book["ISBN"] == isbn:
    #         book.update(book_form)
    #         save_temporary_data(file_handler, lista_ksiazek, saldo, historia)
    #         return book
    # return None
    pass

def change_saldo(amount: float):
    """Changes the current balance by the specified amount."""
    saldo = file_handler.saldo
    if saldo + amount < 0:
        raise ValueError("Cannot set balance to a negative value.")
    saldo += amount
    save_temporary_data(file_handler, file_handler.ksiegozbior, saldo, file_handler.historia)


def borrow_book(borrow_form: dict):
    """Handles borrowing a book by ISBN."""
    isbn = borrow_form.get("isbn")
    autor = borrow_form.get("author", "")
    tytul = borrow_form.get("title", "")
    
    # Find book by ISBN
    for ksiazka in file_handler.ksiegozbior:
        if ksiazka.get("ISBN") == isbn:
            if ksiazka["ilosc_na_stanie"] <= 0:
                raise ValueError("Nie ma tej książki na stanie.")
            
            # Reduce stock and add rental fee
            ksiazka["ilosc_na_stanie"] -= 1
            rental_fee = 10.0  # stała opłata za wypożyczenie
            new_saldo = file_handler.saldo + rental_fee
            
            # Add to history
            historia_entry = f"Wypożyczenie książki: {ksiazka['tytul']}, {ksiazka['autor']}, 1 sztuka"
            file_handler.historia.append(historia_entry)
            
            # Save changes
            save_temporary_data(file_handler, file_handler.ksiegozbior, new_saldo, file_handler.historia)
            return ksiazka
    
    raise ValueError("Taka książka nie istnieje w naszym księgozbiorze.")