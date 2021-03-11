from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float


@dataclass
class StockItem:
    product: Product
    quantity: int

    def withdraw(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"given quantity {quantity} exceded the stock quantity {self.quantity}")

        self.quantity -= quantity

    def add(self, quantity):
        self.quantity += quantity