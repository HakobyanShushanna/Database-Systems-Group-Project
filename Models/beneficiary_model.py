from Models.customer_model import CustomerModel
from Models.bank_model import BankModel

class Beneficiary:
    def __init__(self, beneficiary_id: int, customer: CustomerModel, beneficiary_name: str, beneficiary_account_number: str, bank: BankModel):
        self.beneficiary_id = beneficiary_id
        self.customer = customer
        self.beneficiary_name = beneficiary_name
        self.beneficiary_account_number = beneficiary_account_number
        self.bank = bank