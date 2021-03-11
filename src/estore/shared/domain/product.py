from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float


@dataclass
class StockItem:
    product: Product
    quantity: int