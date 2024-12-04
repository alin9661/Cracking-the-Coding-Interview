from .models import *

class Account:
    def __init__(self,
                 id: int,
                 password: str,
                 name: str,
                 status: AccountStatus,
                 address: Location,
                 email: str,
                 phone: str,
                 ) -> None:
        self.id: int = id
        self.password: str = password
        self.name: str = name
        self.status: AccountStatus = status
        self.address: Location = address
        self.email: str = email
        self.phone: str = phone

    def reset_password(self, new_password: str) -> bool:
        self.password = new_password
        return True
    
class Member(Account):
    def __init__(self, id, password, name, status, address, email, phone):
        super().__init__(id, password, name, status, address, email, phone)

    def availableFundsForTrading(self) -> float:
        return 0.0

class Admin(Account):
    def __init__(self, id, password, name, status, address, email, phone):
        super().__init__(id, password, name, status, address, email, phone)

    def block_member(self, member: Member) -> bool:
        if member.status == AccountStatus.ACTIVE:
            member.status = AccountStatus.BLACKLISTED

        return True

    def unblock_member(self, member: Member) -> bool:
        if member.status != AccountStatus.ACTIVE:
            member.status = AccountStatus.ACTIVE
        else:
            print(f'Member {member.id} is already active')
            return False
        
        return True