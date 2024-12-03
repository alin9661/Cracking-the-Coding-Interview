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
    def __init__(self, 
                 notification_id: int,
                 created_on: datetime,
                 content: str,
                 ) -> None:
        self.notification_id: int = notification_id
        self.created_on: datetime = created_on
        self.content: str = content

    def send_notification(self) -> bool:
        pass

class PostalNotification(Notification):
    def __init__(self, notification_id, created_on, content, address):
        super().__init__(notification_id, created_on, content)
        self.address: str = address

class EmailNotification(Notification):
    def __init__(self, notification_id, created_on, content, email):
        super().__init__(notification_id, created_on, content)
        self.email: str = email


class LibraryCard:
    pass

