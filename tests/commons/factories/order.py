from datetime import date

from estore.shared.domain.order import OrderItem, Order
from factory import Factory, SubFactory, lazy_attribute
from factory.fuzzy import FuzzyInteger, FuzzyFloat, FuzzyDate

from tests.commons.factories.customer import CustomerFactory
from tests.commons.factories.product import ProductFactory


class OrderItemFactory(Factory):
    class Meta:
        model = OrderItem

    product = SubFactory(factory=ProductFactory)
    price = FuzzyFloat(low=0.5, high=5000, precision=2)
    quantity = FuzzyInteger(low=1, high=50)


class OrderFactory(Factory):
    class Meta:
        model = Order

    class Params:
        items_count = 1
        items_params = None

    customer = SubFactory(CustomerFactory)
    created_at = FuzzyDate(start_date=date.today())

    @lazy_attribute
    def items(self):
        if self.items_params:
            return [OrderItemFactory.create(**given_params) for given_params in self.items_params]

        return OrderItemFactory.create_batch(size=self.items_count)
