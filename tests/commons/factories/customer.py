from estore.shared.domain.customer import Customer, Address
from factory import Factory, Faker, List, SubFactory, lazy_attribute


class AddressFactory(Factory):
    class Meta:
        model = Address

    street = Faker("street_name")
    number = Faker("building_number")
    zip_code = Faker("postcode")


class CustomerFactory(Factory):
    class Meta:
        model = Customer

    class Params:
        address_count = 1

    name = Faker("name")
    social_number = Faker("ssn")

    @lazy_attribute
    def addresses(self):
        return AddressFactory.create_batch(size=self.address_count)
