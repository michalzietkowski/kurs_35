class InventoryManager:
    def __init__(self):
        # Początkowy stan magazynu
        self._stock = {
            "Laptop": 5,
            "Smartfon": 3,
            "Tablet": 2
        }

    def check_availability(self, product: str, quantity: int) -> bool:
        return self._stock.get(product, 0) >= quantity

    def update_stock(self, product: str, quantity: int) -> None:
        if product in self._stock:
            self._stock[product] -= quantity

    def get_stock(self):
        return self._stock.copy()
