from Models.bank_model import BankModel
from Models.employee_model import EmployeeModel

class Branch:
    def __init__(self, branch_id: int, branch_name: str, location: str, contact_number: str, bank: BankModel, manager: EmployeeModel):
        self.branch_id = branch_id
        self.branch_name = branch_name
        self.location = location
        self.contact_number = contact_number
        self.bank = bank
        self.manager = manager