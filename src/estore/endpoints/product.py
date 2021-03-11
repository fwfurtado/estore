from estore.schemas.http.forms.product import CreationProduct, StockUpdate
from estore.schemas.http.views.product import Product
from fastapi import APIRouter, HTTPException
from typing import List


admin = APIRouter(prefix='/admin/products')

@admin.post(path="/", status_code=201)
def create_product(product_form: CreationProduct) -> Product:
    return Product(id=1, in_stock=0, name=product_form.name, price=product_form.price)

@admin.put(path="/{product_id}/receive", status_code=202)
def add_product_quantity_to_stock(product_id: int, stock_form: StockUpdate) -> Product:
    return Product(id=product_id, name="Fake name", price=0.5, in_stock=stock_form.quantity)

@admin.put(path="/{product_id}/withdraw", status_code=202)
def withdraw_product_quantity_from_stock(product_id, stock_form: StockUpdate) -> Product:
    return Product(id=product_id, name="Fake name", price=0.5, in_stock=stock_form.quantity)

@admin.get("/")
def list_all_products() -> List[Product]:
    return []

@admin.get("/{product_id}")
def show_product_details(product_id: int) -> Product:
    return Product(id=product_id, name="Fake Name", price=0.5, in_stock=1)

