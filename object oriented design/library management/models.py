from enum import Enum

class BookFormat(Enum):
    HARDCOVER = 1
    PAPERBACK = 2
    AUDIOBOOK = 3
    EBOOK = 4
    NEWSPAPER = 5
    MAGAZINE = 6
    JOURNAL = 7

class BookStatu(Enum):
    AVAILABLE = 1
    RESERVED = 2
    LOANED = 3
    LOST = 4

class ReservationStatus(Enum):
    WAITING = 1
    PENDING = 2
    COMPLETED = 3
    CANCELLED = 4
    NONE = 5

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELLED = 3
    BLACKLISTED = 4
    NONE = 5

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