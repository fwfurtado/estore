from estore.shared.domain.product import Product
from factory import Factory
from factory.fuzzy import FuzzyFloat, FuzzyText


class ProductFactory(Factory):
    class Meta:
        model = Product

    name = FuzzyText(prefix="product-", length=10)
    price = FuzzyFloat(low=0.5, high=5000, precision=2)
