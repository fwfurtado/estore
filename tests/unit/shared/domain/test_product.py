import pytest

from tests.commons.factories.product import StockItemFactory


def test_should_increase_stock_quantity(faker):
    item = StockItemFactory.create()
    initial_quantity = item.quantity

    item.add(quantity=faker.pyint(min_value=1, max_value=5000))

    assert item.quantity > initial_quantity


def test_should_decrease_stock_quantity():
    item = StockItemFactory.create()
    initial_quantity = item.quantity
    decreased_value = initial_quantity - 1

    item.withdraw(quantity=decreased_value)

    assert item.quantity < initial_quantity


def test_should_raise_an_error_when_trying_to_withdraw_an_excess_amount():
    item = StockItemFactory.create()
    initial_quantity = item.quantity
    decreased_value = initial_quantity + 1

    with pytest.raises(ValueError):
        item.withdraw(decreased_value)
