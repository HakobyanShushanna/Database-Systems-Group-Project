from Models.customer_model import CustomerModel
from typing import Optional
from datetime import datetime

class TransactionModel:
    def __init__(self, transaction_id: int, sender: CustomerModel, receiver: CustomerModel, amount: float, description: Optional[str], type: str, transaction_date: Optional[datetime] = None):
        self.transaction_id = transaction_id
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.description = description
        self.type = type
        self.transaction_date = transaction_date or datetime.now()