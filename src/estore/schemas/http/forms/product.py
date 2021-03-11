from pydantic import BaseModel

class CreationProduct(BaseModel):
    name: str
    price: float

class  StockUpdate(BaseModel):
    quantity: int