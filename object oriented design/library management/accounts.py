## Account Management
class Account:
    def __init__(self,
                 id: str,
                 password: str,
                 status: AccountStatus,
                 person: Person
                 ) -> None:
        self.id: str = id
        self.password: str = password
        self.status: AccountStatus = status
        self.person: Person = person

    def reset_password(self, new_password) -> bool:
        self.password = new_password

class Librarian(Account):
    def __init__(self, id, password, status, person) -> None:
        super().__init__(id, password, status, person)

    def add_book_item(self, book_item: BookItem) -> bool:
        pass

    def block_member(self) -> bool:
        pass

    def unblock_member(self) -> bool:
        pass

class Member(Account):
    def __init__(self, id, password, status, person, membership_date, books_checked_out) -> None:
        super().__init__(id, password, status, person)