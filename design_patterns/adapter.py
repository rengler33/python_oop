"""Demostration of the (Object) Adapter pattern. Category: structural.

An adapter pattern is used to adapt the interface of a class
to be used as another interface. This can be useful to make
existing classes work with other similar classes, without the
need to modify existing classes.

Note: this is an example of an object-based (composition) approach.
There is an alternative class-based (inheritance) approach possible
that is not shown here.

This example assumes there are two types of customer objects.
Each customer object has its own way of storing name and phone
number. The goal is to have a single interface for all customers.
"""

from abc import ABC, abstractmethod


class LegacyCustomer:
    """Example of first type of customer - stores first and last name separately"""

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


class ThirdPartyCustomer:
    """Example of another customer type - stores area code and short phone number separately"""

    def __init__(self, name, area_code, phone_number):
        self.name = name
        self.area_code = area_code
        self.phone_number = phone_number


class CustomerAdapter(ABC):
    """Example of how we'd like to interact with customers - name should return full name
    and phone should return full phone number
    """

    @property
    @abstractmethod
    def name(self):
        """Full name of customer"""

    @property
    @abstractmethod
    def phone(self):
        """Full phone number of customer"""


class LegacyAdapter(CustomerAdapter):
    def __init__(self, customer: LegacyCustomer):
        self._customer = customer

    @property
    def name(self):
        return f"{self._customer.first_name} {self._customer.last_name}"

    @property
    def phone(self):
        return self._customer.phone_number


class ThirdPartyAdapter(CustomerAdapter):
    def __init__(self, customer: ThirdPartyCustomer):
        self._customer = customer

    @property
    def name(self):
        return self._customer.name

    @property
    def phone(self):
        return f"{self._customer.area_code}-{self._customer.phone_number}"


if __name__ == "__main__":
    customer_a = LegacyAdapter(
        LegacyCustomer(first_name="Bob", last_name="Smith", phone_number="555-321-9876")
    )
    customer_b = ThirdPartyAdapter(
        ThirdPartyCustomer(name="Jackie Crusoe", area_code="555", phone_number="777-5432")
    )

    # interact with customer objects with the interface defined by the CustomerAdapter 
    for customer in [customer_a, customer_b]:
        print(customer.name)
        print(customer.phone)
