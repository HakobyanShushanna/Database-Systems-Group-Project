from Models.employee_model import EmployeeModel
from typing import Optional
from datetime import date

class AuditLog:
    def __init__(self, log_id: int, employee: EmployeeModel, action: str, log_date: Optional[date] = None, ip_address: str = "0.0.0.0"):
        self.log_id = log_id
        self.employee = employee
        self.action = action
        self.log_date = log_date or date.today()
        self.ip_address = ip_address