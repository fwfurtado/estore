from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    id: int
    street: str
    number: Optional[int]
    zip_code: str

class SimpleAddress(BaseModel):
    id: int
    full_address: str

class Customer(BaseModel):
    id: int
    name: str
    social_number: str
    addresses: Optional[List[SimpleAddress]]
