from Models.bank_model import BankModel
from typing import Optional
from datetime import datetime

class AccountModel:
    def __init__(self, account_id: int, balance: float, status: str, account_type: str, created_at: datetime, bank: Optional[BankModel] = None):
        self.account_id = account_id
        self.balance = balance
        self.status = status
        self.account_type = account_type
        self.created_at = created_at
        self.bank = bank