from Models.transaction_model import TransactionModel
from datetime import date

class PaymentModel:
    def __init__(self, payment_id: int, transaction: TransactionModel, payment_date: date, amount: float, payment_method: str):
        self.payment_id = payment_id
        self.transaction = transaction
        self.payment_date = payment_date
        self.amount = amount
        self.payment_method = payment_method