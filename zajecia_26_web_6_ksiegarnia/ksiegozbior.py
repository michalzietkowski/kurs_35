
from file_handler import file_handler, save_temporary_data
from models import db, Saldo, Book, History


def get_books():
    """Returns the list of books in the collection."""
    return file_handler.ksiegozbior

def get_bookstore_state():
    saldo = db.session.query(Saldo).first()
    ksiegozbior = db.session.query(Book).all()
    print(ksiegozbior)
    historia = db.session.query(History).all()
    """Returns the current state of the bookstore, including balance and history."""
    return {
        "saldo": saldo.amount,
        "historia": historia,
        "ksiegozbior": ksiegozbior,
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
    book_for_db = Book(
        title= new_book.get("tytul"),
        author= new_book.get("autor"),
        price= new_book.get("cena"),
        amount=new_book.get("ilosc"),
        amount_available=new_book.get("ilosc_na_stanie"),
        category=new_book.get("kategoria"),
        isbn=new_book.get("ISBN"),
        year=float(new_book.get("rok_wydania")),
    )
    saldo = db.session.query(Saldo).first()
    price_to_substract = new_book.get("cena") * new_book.get("ilosc")
    if saldo.amount < price_to_substract:
        raise ValueError("Nie można dodać książki, ponieważ saldo jest zbyt niskie.")
    saldo.amount -= price_to_substract
    db.session.add(saldo)
    db.session.add(book_for_db)
    db.session.commit()

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