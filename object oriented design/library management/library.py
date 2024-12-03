import datetime
from models import *

class Library:
    def __init__(self, name, address) -> None:
        self.name: str = name
        self.address: str = address

    def get_address(self) -> str:
        return self.address




class Catalog:
    pass

class Fine:
    pass

class Author:
    def __init__(self,
                 name: str,
                 description: str
                 ) -> None:
        self.name: str = name
        self.description: str = name
        
    def get_name(self) -> str:
        return self.name


## Notifications
class Notification:
    pass

class PostalNotification(Notification):
    pass

class EmailNotification(Notification):
    pass


class LibraryCard:
    pass

