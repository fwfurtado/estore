from estore.shared.domain.product import Product, StockItem
from factory import Factory, SubFactory
from factory.fuzzy import FuzzyFloat, FuzzyText, FuzzyInteger


class ProductFactory(Factory):
    class Meta:
        model = Product

    name = FuzzyText(prefix="product-", length=10)
    price = FuzzyFloat(low=0.5, high=5000, precision=2)


class StockItemFactory(Factory):
    class Meta:
        model = StockItem

    product = SubFactory(ProductFactory)
    quantity = FuzzyInteger(low=1, high=5000)
