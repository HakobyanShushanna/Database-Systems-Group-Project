from Models.person_model import PersonModel
from Models.bank_model import BankModel
from typing import Optional
from datetime import date

class CustomerModel(PersonModel):
    def __init__(self, customer_id: int, first_name: str, middle_name: Optional[str], last_name: str, role: str, phone: str, email: str, date_of_birth: date, address: str, bank: BankModel, created_at:date):
        super().__init__(customer_id, first_name, middle_name, last_name, role, phone, email)
        self.date_of_birth = date_of_birth
        self.created_at = created_at
        self.address = address
        self.bank = bank