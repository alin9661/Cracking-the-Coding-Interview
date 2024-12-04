from enum import Enum
from abc import ABC

class OrderStatus(Enum):
    OPEN, FILED, PARTIALLY_FILLED, CANCELLED = 1, 2, 3, 4

class TimeEnforcementType(Enum):
    GOOD_TILL_CANCELLED, FILL_OR_KILL, IMMEDIATE_OR_CANCEL, ON_THE_OPEN, ON_THE_CLOSE = 1, 2, 3, 4, 5

class AccountStatus(Enum):
    ACTIVE, CLOSED, CANCELLED, BLACKLISTED, NONE = 1, 2, 3, 4, 5

class ReturnStatus(Enum):
    SUCCESS, FAIL, INSUFFICIENT_FUNDS, INSUFFICIENT_QUANTITY, NO_STOCK_POSITION = 1, 2, 3, 4, 5

class Location(ABC):
    def __init__(self,
                 street_address: str,
                 city: str,
                 state: str,
                 zipcode: str,
                 country: str
                 ) -> None:
        super().__init__()
        self.street_address: str = street_address
        self.city: str = city
        self.state: str = state
        self.zipcode: str = zipcode
        self.countr: str = country