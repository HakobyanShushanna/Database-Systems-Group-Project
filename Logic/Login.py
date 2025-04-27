from config import execute_query, get_query
from Logic.ceasar import decrypt
from Logic.Registration import load_user
from static_files import login
from Models.bank_model import BankModel
from Models.customer_model import CustomerModel
from Models.employee_model import EmployeeModel
from Models.position_model import PositionModel


def login_user(username: str, password: str):
    login_query = get_query("Get login info", login)  # Fixed the query name to "Login"
    if login_query is None:
        return None, "Login query not found."

    row = execute_query(login_query, (username,), return_row=True)
    if row is None:
        return None, "Invalid username or password."

    person_id, encrypted_password = row
    decrypted_password = decrypt(encrypted_password, 3)

    if password != decrypted_password:
        return None, "Invalid username or password."

    # Checking if the user is a customer
    customer_query = get_query("Is Customer", login)
    is_customer = execute_query(customer_query, (person_id,), return_row=True)

    if is_customer:
        # Load customer data
        user = load_user(person_id, "Customer")
        return user, "customer"

    # Checking if the user is an employee
    employee_query = get_query("Is Employee", login)
    is_employee = execute_query(employee_query, (person_id,), return_row=True)

    if is_employee:
        # Load employee data
        user = load_user(person_id, "Employee")
        return user, "employee"

    return None, "User not found."


def load_customer(person_id: int):
    # Assuming the query is fetched and passed from somewhere else
    customer_data = execute_query("Get customer data", person_id)  # Query will be fetched and handled in the config

    if customer_data is None:
        return None

    # Assuming the result is returned as a tuple with the necessary fields
    customer_id, first_name, middle_name, last_name, role, phone, email, date_of_birth, address, bank_id, created_at = customer_data

    # Fetch bank data similarly from the config or an external source
    bank_data = execute_query("Get bank data", bank_id)
    if bank_data is None:
        return None

    bank_id, bank_name, bank_address = bank_data
    bank = BankModel(bank_id, bank_name, bank_address)

    # Create and return the CustomerModel
    customer = CustomerModel(
        customer_id=customer_id,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        role=role,
        phone=phone,
        email=email,
        date_of_birth=date_of_birth,
        address=address,
        bank=bank,
        created_at=created_at
    )

    return customer


def load_employee(person_id: int):
    # Assuming the query is fetched and passed from somewhere else
    employee_data = execute_query("Get employee data", person_id)  # Query will be handled externally

    if employee_data is None:
        return None

    # Assuming the result is returned as a tuple with the necessary fields
    employee_id, first_name, middle_name, last_name, role, phone, email, position_id = employee_data

    # Fetch position data similarly from the config or external query handler
    position_data = execute_query("Get position data", position_id)
    if position_data is None:
        return None

    position_id, position_name, position_description = position_data
    position = PositionModel(position_id, position_name, position_description)

    # Create and return the EmployeeModel
    employee = EmployeeModel(
        employee_id=employee_id,
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        role=role,
        phone=phone,
        email=email,
        position=position
    )

    return employee
