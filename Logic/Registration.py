from yaml import safe_load_all

from config import execute_query, get_query
import streamlit as st
import re
from datetime import datetime, date

filename = "CRUD.sql"

def format_phone(phone:str):
    phone = re.sub(r'\D', '', phone)
    if phone.startswith("0"):
        phone = phone[1:]
    if not phone.startswith("374"):
        phone = "374" + phone

    phone = "+" + phone

    return phone


def register_person(first_name:str, middle_name:str, last_name:str, role:str, email:str, phone:str):
    phone = format_phone(phone)

    query = get_query("Register person", filename)
    if query is None:
        st.error("No query found for registering person.")
        return

    params = (first_name, middle_name, last_name, role, phone, email)

    person_id = execute_query(query, params)

    return person_id


def register_customer(first_name:str, middle_name:str, last_name:str, dob:date, email:str, address:str, phone:str, selected_bank_id):
    person_id = register_person(first_name, middle_name, last_name, "customer", email, phone)

    if person_id is None:
        st.error("Error registering person.")
        return

    customer_query = get_query("Register customer", "CRUD.sql")
    if customer_query is None:
        st.error("No query found for registering customer.")
        return

    customer_params = (person_id, dob, datetime.now(), address, selected_bank_id)

    execute_query(customer_query, customer_params)
    st.success("User registered successfully.")


def register_employee(first_name:str, middle_name:str, last_name:str, role:str, phone:str, email:str, selected_role_id:int):
    person_id = register_person(first_name, middle_name, last_name, role, email, phone)

    if person_id is None:
        st.error("Error registering person.")
        return

    employee_query = get_query("Register employee", "CRUD.sql")
    if employee_query is None:
        st.error("No query found for registering employee.")
        return


    employee_params = (person_id, selected_role_id)

    execute_query(employee_query, employee_params)
    st.success("User registered successfully.")