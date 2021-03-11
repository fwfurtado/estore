from tests.commons.factories.order import OrderFactory


def test_should_return_the_total_of_order_based_on_their_items():
    order = OrderFactory.create(items_params=[{"quantity": 1, "price": 125}, {"quantity": 1, "price": 132}])
    order_total = 257

    assert order.total == order_total

