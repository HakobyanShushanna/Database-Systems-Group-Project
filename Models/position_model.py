from Models.bank_model import BankModel
from typing import Optional

class PositionModel:
    def __init__(self, position_id: int, position_name: str, salary: float, bank: Optional[BankModel] = None):
        self.position_id = position_id
        self.position_name = position_name
        self.salary = salary
        self.bank = bank