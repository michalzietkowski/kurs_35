from abc import ABC, abstractmethod


class DiscountCalculator:
    def calculate_discount(self, price: float, discount_type: str) -> float:
        if discount_type == 'percent':
            return price * 0.1
        elif discount_type == 'fixed':
            return 10.0
        elif discount_type == 'vip':
            return price * 0.2
        elif discount_type == 'normal':
            return 0.0

class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, price: float) -> float:
        pass


class VipDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.2

class FixedDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return 10.0

class PercentDiscount(DiscountStrategy):
    def calculate_discount(self, price: float) -> float:
        return price * 0.1

class DiscountCalculator:
    def __init__(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def calculate_discount(self, price: float) -> float:
        return self.strategy.calculate_discount(price)