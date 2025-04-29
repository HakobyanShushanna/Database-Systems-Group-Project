from BackEnd.common_functions import get_query, execute_query, add_person
from datetime import datetime, timezone
from static_variables import crud, search_filter


def __format_person(person):
    return f"{person[1]} {person[2] if person[2] else ""} {person[3]} (ID = {person[0]})"


def add_employee(first_name:str, middle_name:str, last_name:str, role:str, phone:str, email:str, position_id:int, branch_id:int):
    employee_id = add_person(first_name, middle_name, last_name, role, phone, email)

    if not employee_id:
        return False

    employee_query = get_query("Add employee", crud)

    if not employee_query:
        return False, "Employee query not found"

    params = (employee_id, position_id, )
    success = execute_query(employee_query, params)

    if not success:
        return False, "Something went wrong while adding the employee"

    branch_employee_query = get_query("Add branch_employee", crud)

    if not branch_employee_query:
        return False, "Employee & Branch query not found"

    params = (branch_id, employee_id, )
    success = execute_query(branch_employee_query, params)

    if success:
        return success, "Employee added successfully"
    return success, "Something went wrong while connecting the employee to the branch"


def add_customer(first_name:str, middle_name:str, last_name:str, role:str, phone:str, email:str, date_of_birth:datetime, address, bank_id):
    customer_id = add_person(first_name, middle_name, last_name, role, phone, email)

    if not customer_id:
        return False

    customer_query = get_query("Add customer", crud)

    if not customer_query:
        return False, "Customer query not found"

    params = (customer_id, date_of_birth, address, bank_id,)
    success = execute_query(customer_query, params)

    if success:
        return success, "Customer added successfully"
    return success, "Something went wrong while adding the Customer"


def add_activity(employee_id:int, action:str, ip_address:str):
    query = get_query("Add audit_log", crud)

    if not query:
        return False, "Query Add audit_log does not exist"

    params = (employee_id, action, datetime.now(timezone.utc), ip_address)
    result = execute_query(query, params)

    if result:
        return result, "Action added successfully"
    return result, "Something went wrong while adding an action"


def get_customers():
    query = get_query("Customers for admin", search_filter)

    if not query:
        return False, "Customers for admin query not found"

    customers_list = execute_query(query, fetch_all=True)
    customers_list = {__format_person(person):person[0] for person in customers_list}
    return customers_list


def get_employees():
    query = get_query("Employees list", search_filter)

    if not query:
        return False, "Employees list query not found"

    employees_list = execute_query(query, fetch_all=True)
    employees_list = {__format_person(person):person[0] for person in employees_list}

    return employees_list