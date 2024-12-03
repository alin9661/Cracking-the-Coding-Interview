import datetime

class Fine:
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount

class FineTransaction:
    def __init__(self,
                 creation_date: datetime,
                 amount: float
                 ) -> None:
        self.creation_date = creation_date
        self.amount = amount

class CreditCardTransaction(FineTransaction):
    def __init__(self, creation_date, amount, name_on_card: str):
        super().__init__(creation_date, amount)
        self.name_on_card: str = name_on_card

class CheckTransaction(FineTransaction):
    def __init__(self, creation_date, amount, bank_name: str, check_number: str):
        super().__init__(creation_date, amount)
        self.bank_name: str = bank_name
        self.check_number: str = check_number

class CashTransaction(FineTransaction):
    def __init__(self, creation_date, amount, cash_tendered: float):
        super().__init__(creation_date, amount)
        self.cash_tendered: float = cash_tendered