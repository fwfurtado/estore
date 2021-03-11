from dataclasses import dataclass, field
from datetime import  date
from typing import List
from estore.shared.domain.product import  Product
from estore.shared.domain.customer import Customer

@dataclass(frozen=True)
class OrderItem:
    product: Product
    price: float
    quantity: int

    @property
    def total(self):
        return self.price * self.quantity

@dataclass(frozen=True)
class Order:
    customer: Customer
    created_at: date
    items: List[OrderItem]

    def add_item(self, item: OrderItem):
        self.items.append(item)

    @property
    def total(self):
        return sum(item.total for item in self.items)