import datetime
from models import *

## Books
class Book:
    def __init__(self, isbn, title, subject, publisher, language, pages) -> None:
        self.isbn: str =  isbn
        self.title: str =  title
        self.subject: str =  subject
        self.publisher : str = publisher
        self.language: str = language
        self.num_pages: int = pages

    def get_title(self) -> str:
        return self.title

class BookItem(Book):
    def __init__(self,
                 barcode: str,
                 is_reference: bool,
                 borrowed: datetime,
                 due_date: datetime,
                 price: float,
                 format: Book,
                 status,
                 date_purchased: datetime,
                 publication_date: datetime
                 ) -> None:
        self.barcode: str = barcode
        self.is_reference: bool = is_reference
        self.borrowed: datetime = borrowed
        self.due_date: datetime = due_date
        self.price: float = price
        self.format: Book = format
        self.status = status
        self.date_purchased: datetime = date_purchased
        self.publication_date: datetime = publication_date

    def checkout(self) -> bool:
        pass

class BookReservation:
    def __init__(self, 
                 creation_date: datetime,
                 status: ReservationStatus
                 ) -> None:
        self.creation_date: datetime = creation_date
        self.status: ReservationStatus = status

class BookLending:
    def __init__(self,
                 creation_date: datetime,
                 due_date: datetime,
                 return_date: datetime
                 ) -> None:
        self.creation_date: datetime = creation_date
        self.due_date: datetime = due_date
        self.return_date: datetime = return_date

    def get_return_date(self) -> datetime:
        return self.return_date
    

class Rack:
    def __init__(self, number: int, location_identifier: str) -> None:
        self.number: int = number
        self.location_identifier: str = location_identifier