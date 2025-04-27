from Models.loan_model import LoanModel
from typing import Optional
from datetime import date

class LoanRepaymentModel:
    def __init__(self, repayment_id: int, loan: LoanModel, repayment_date: date, amount_paid: float, remaining_balance: float, created_at: Optional[date] = None):
        self.repayment_id = repayment_id
        self.loan = loan
        self.repayment_date = repayment_date
        self.amount_paid = amount_paid
        self.remaining_balance = remaining_balance
        self.created_at = created_at or date.today()