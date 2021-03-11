from pydantic import BaseModel
from typing import Optional

class CreationCustomer(BaseModel):
    name: str
    social_number: str

class AddressUpdate(BaseModel):
    street: str
    number: Optional[int]
    zip_code: str