from Models.person_model import PersonModel
from Models.position_model import PositionModel
from typing import Optional

class EmployeeModel(PersonModel):
    def __init__(self, employee_id: int, first_name: str, middle_name: Optional[str], last_name: str, role: str, phone: str, email: str, position: Optional[PositionModel] = None):
        super().__init__(employee_id, first_name, middle_name, last_name, role, phone, email)
        self.position = position