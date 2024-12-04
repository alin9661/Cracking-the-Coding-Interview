import datetime
from models import *
from typing import Dict

class Library:
    def __init__(self, name, address) -> None:
        self.name: str = name
        self.address: str = address

    def get_address(self) -> str:
        return self.address

class LibraryCard:
    def __init__(self,
                 card_number: str,
                 barcode: str,
                 issued_at: datetime,
                 active: bool
                 ) -> None:
        self.card_number: str = card_number
        self.barcode: str = barcode
        self.issued_at: datetime = issued_at
        self.active: bool = active

class BarcodeReader:
    def __init__(self,
                 id: str,
                 registed_at: datetime,
                 active: bool
                 ) -> None:
        self.id: str = id
        self.registered_at: datetime = registed_at
        self.active: bool = active

    def is_active(self) -> bool:
        return self.active

class Catalog(Search):
    def __init__(self,
                 creation_date: datetime,
                 total_books: int,
                 book_titles: Dict[str, list],
                 book_authors: Dict[str, list],
                 book_subjects: Dict[str, list],
                 book_publication_dates: Dict[datetime, list],
                 ) -> None:
        self.creation_date: datetime = creation_date
        self.total_books: int = total_books
        self.book_titles: Dict[str, list] = book_titles
        self.book_authors: Dict[str, list] = book_authors
        self.book_subjects: Dict[str, list] = book_subjects
        self.book_publication_dates: Dict[datetime, list] = book_publication_dates

    def update_catalog(self) -> bool:
        pass

    def search_by_title(self, query):
        return self.__book_titles.get(query)

    def search_by_author(self, query):
        return self.__book_authors.get(query)

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
