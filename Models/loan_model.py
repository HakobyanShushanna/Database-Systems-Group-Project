from typing import Optional
from Models.customer_model import CustomerModel
from datetime import date

class LoanModel:
    def __init__(self, loan_id: int, customer: CustomerModel, loan_type: str, amount: float, issued_date: date, due_date: date, interest_rate: float, status: str, created_at: Optional[date] = None):
        self.loan_id = loan_id
        self.customer = customer
        self.loan_type = loan_type
        self.amount = amount
        self.issued_date = issued_date
        self.due_date = due_date
        self.interest_rate = interest_rate
        self.status = status
        self.created_at = created_at or date.today()