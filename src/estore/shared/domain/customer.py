from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Address:
    street: str
    number: Optional[int]
    zip_code: str


@dataclass
class Customer:
    name: str
    social_number: str
    addresses: List[Address]
