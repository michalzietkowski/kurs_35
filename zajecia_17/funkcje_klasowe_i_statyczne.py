class Programista:

    jezyk = "polski"
    leniwy = True

    def __init__(self, imie, jezyk_programowania):
        self.imie = imie
        self.jezyk_programowania = jezyk_programowania

    def zmien_imie(self, nowe_imie):
        self.imie = nowe_imie

    def zmien_jezyk(self, nowy_jezyk):
        self.jezyk = nowy_jezyk

    @classmethod
    def zmien_bycie_leniwym(cls):
        if cls.leniwy:
            cls.leniwy = False
        else:
            cls.leniwy = True

    @staticmethod
    def przywitaj_sie():
        print("Przywitaj sie")


pierwszy_programista = Programista("Jan", "Python")
drugi_programista = Programista("Anna", "Java")

# print(id(pierwszy_programista))
# print(id(drugi_programista))
#
# print(pierwszy_programista.jezyk_programowania)
# print(drugi_programista.jezyk_programowania)
# print(pierwszy_programista.jezyk)
# print(drugi_programista.jezyk)
# print(pierwszy_programista.leniwy)
# print(drugi_programista.leniwy)

# print(id(pierwszy_programista.jezyk))
# print(id(drugi_programista.jezyk))
# print(id(pierwszy_programista.leniwy))
# print(id(drugi_programista.leniwy))
#
# pierwszy_programista.zmien_bycie_leniwym()
#
# print(pierwszy_programista.leniwy)
# print(drugi_programista.leniwy)
#
# print(id(pierwszy_programista.leniwy))
# print(id(drugi_programista.leniwy))

print(id(pierwszy_programista.przywitaj_sie))
print(id(drugi_programista.przywitaj_sie))

maszyna_ai = Programista


chat_gpt = maszyna_ai("ChatGPT", "Python")

glupie_wywolanie = chat_gpt.przywitaj_sie

glupie_wywolanie()
print(chat_gpt.imie)
print(chat_gpt.jezyk_programowania)