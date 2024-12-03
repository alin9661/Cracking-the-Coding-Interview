from enum import Enum

class BookFormat(Enum):
    pass

class BookStatu(Enum):
    pass

class ReservationStatus(Enum):
    pass

class AccountStatus(Enum):
    pass

class Address:
    def __init__(self,
                 street_address: str,
                 city: str,
                 state: str,
                 zipcode: str,
                 country: str
                 ) -> None:
        self.street_address: str = street_address
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        self.country: str = country

class Person:
    def __init__(self,
                 name: str,
                 address: Address,
                 email: str,
                 phone: str,
                 ) -> None:
        self.name: str = name
        self.address: Address = address
        self.email: str = email
        self.phone: str = phone