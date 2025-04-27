import streamlit as st
import re
from datetime import datetime, date
from config import get_query, execute_query
from Models.customer_model import CustomerModel
from Models.bank_model import BankModel
from Models.employee_model import EmployeeModel
from Models.position_model import PositionModel

crud = "Sql/CRUD.sql"
search_filter = "Sql/SearchFilter.sql"

def banks_list():
    query = get_query("Banks list", search_filter)
    if query is None:
        st.error("No query found")
        return {}

    banks = execute_query(query, fetch_all=True)
    bank_options = {name: bank_id for bank_id, name in banks}
    return bank_options

def roles_list(bank_id):
    query = get_query("Roles list", search_filter)
    if query is None:
        st.error("No query found")
        return {}

    roles = execute_query(query, (bank_id,), fetch_all=True)
    role_options = {name: role_id for role_id, name in roles}
    return role_options

def branches_list(bank_id):
    query = get_query("Branches list", search_filter)
    if query is None:
        st.error("No query found")
        return {}

    branches = execute_query(query, (bank_id,), fetch_all=True)
    branch_options = {name: branch_id for branch_id, name in branches}
    return branch_options

def load_user(person_id, role: str):
    query = get_query(role, search_filter)
    if query is None:
        st.error("Query not found for user_query")
        return None

    row = execute_query(query, (person_id,), return_row=True)

    if not row:
        return None

    if role == "Customer":
        return CustomerModel(
            customer_id=row[0],
            date_of_birth=row[1],
            address=row[3],
            bank=BankModel(row[4], None, None, None),
            created_at=row[2],
            first_name=row[6],
            middle_name=row[7],
            last_name=row[8],
            role=row[9],
            phone=row[10],
            email=row[11]
        )
    elif role == "Employee":
        return EmployeeModel(
            employee_id=row[0],
            first_name=row[3],
            middle_name=row[4],
            last_name=row[5],
            role=row[6],
            phone=row[7],
            email=row[8],
            position=PositionModel(row[1], None) if row[1] else None
        )

    return None

def format_phone(phone: str):
    phone = re.sub(r'\D', '', phone)
    if phone.startswith("0"):
        phone = phone[1:]
    if not phone.startswith("374"):
        phone = "374" + phone
    return "+" + phone

def register_person(first_name: str, middle_name: str, last_name: str, role: str, email: str, phone: str):
    phone = format_phone(phone)
    query = get_query("Register person", crud)
    if query is None:
        st.error("No query found for registering person.")
        return None

    params = (first_name, middle_name, last_name, role, phone, email)
    person_id = execute_query(query, params)
    return person_id

def register_customer(first_name: str, middle_name: str, last_name: str, dob: date, email: str, address: str, phone: str, selected_bank_id):
    person_id = register_person(first_name, middle_name, last_name, "customer", email, phone)
    if person_id is None:
        st.error("Error registering person.")
        return

    customer_query = get_query("Register customer", crud)
    if customer_query is None:
        st.error("No query found for registering customer.")
        return

    customer_params = (person_id, dob, datetime.now(), address, selected_bank_id)
    execute_query(customer_query, customer_params)

    # ✅ After successful registration, load the full user and store it
    st.session_state.user = load_user(person_id, "Customer")
    st.session_state.page = "my_profile"
    st.rerun()

def register_employee(first_name: str, middle_name: str, last_name: str, role: str, phone: str, email: str, selected_role_id: int):
    person_id = register_person(first_name, middle_name, last_name, role, email, phone)
    if person_id is None:
        st.error("Error registering person.")
        return

    employee_query = get_query("Register employee", crud)
    if employee_query is None:
        st.error("No query found for registering employee.")
        return

    employee_params = (person_id, selected_role_id)
    execute_query(employee_query, employee_params)

    # ✅ Load user and save to session
    st.session_state.user = load_user(person_id, "Employee")
    st.session_state.page = "my_profile_employee"
    st.rerun()