import pytest


@pytest.mark.regression #Every test inside of the class is marked regression
class TestCheckout:

    def test_checkout_as_guest(self):
        print("Checkout guest")

    def test_checkout_existing_user(self):
        print("Checkout existing user")

