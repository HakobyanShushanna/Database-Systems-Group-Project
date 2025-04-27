from typing import Optional

class PersonModel:
    def __init__(self, id: int, first_name: str, middle_name: Optional[str], last_name: str, role: str, phone: str, email: str):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.role = role
        self.phone = phone
        self.email = email