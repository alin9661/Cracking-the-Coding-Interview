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

class Rack:
    pass

class BookReservation:
    pass

class BookLending:
    pass