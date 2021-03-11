from estore.schemas.http.forms.customer import CreationCustomer, AddressUpdate
from estore.schemas.http.views.customer import Customer, Address
from fastapi import APIRouter

router = APIRouter(prefix="/customers")


@router.post("/", status_code=201)
def create_customer(customer_form: CreationCustomer) -> Customer:
    return customer_form

@router.put("/{customer_id}/address", status_code=202)
def add_address_to_customer(customer_id: int, address_form: AddressUpdate) -> Address:
    return

@router.put("/{customer_id}/address/{address_id}", status_code=202)
def update_an_address_of_customer(customer_id: int, address_id: int, address_form: AddressUpdate) -> Address:
    return

@router.delete("/{custormer_id}/address/{address_id}", status_code=204)
def remove_an_address_of_customer(customer_id: int, address_id: int):
    return

@router.get("/{customer_id}")
def show_customer(customer_id: int) -> Customer:
    return