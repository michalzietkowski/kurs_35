def funkcja_kwadratowa(liczba):
    return liczba ** 2

def dodaj(a, b):
    return a + b

print(funkcja_kwadratowa(5))
print(dodaj(3, 4))

# Lambda functions
# nazwa_funkcji = lambda liczba: dodaj(3, liczba)

funkcja_kwadratowa_lambda = lambda liczba: liczba ** 2

funkcja_dodaj_lambda = lambda a, b: a + b

print(funkcja_kwadratowa_lambda(5))
print(funkcja_dodaj_lambda(3, 4))