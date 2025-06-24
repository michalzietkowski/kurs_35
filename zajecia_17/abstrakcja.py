from abc import ABC, abstractmethod

# class FiguraGeometryczna(ABC):
#
#     @abstractmethod
#     def oblicz_pole(self):
#         return None
#
#     @abstractmethod
#     def oblicz_obwod(self):
#         return None
#
# class Trojkat(FiguraGeometryczna):
#     def __init__(self, podstawa, wysokosc):
#         self.podstawa = podstawa
#         self.wysokosc = wysokosc
#
#     def oblicz_pole(self):
#         return 0.5 * self.podstawa * self.wysokosc
#
#     def oblicz_obwod(self):
#         return self.podstawa + 2 * ((self.podstawa / 2) ** 2 + self.wysokosc ** 2) ** 0.5
#
#
# trojkat = Trojkat(podstawa=1, wysokosc=2)


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

class BlikPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"Processing BLIK payment of {amount} PLN"


class CardPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"Processing card payment of {amount} PLN"

class PayPalPayment(Payment):
    def process_payment(self, amount: float) -> str:
        return f"Processing PayPal payment of {amount} PLN"

