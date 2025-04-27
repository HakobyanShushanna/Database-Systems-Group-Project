import streamlit as st
import Logic.Registration
from config import get_query, execute_query
from datetime import datetime

filename = "SearchFilter.sql"


def banks_list():
    query = get_query("Banks list", filename)
    if query is None:
        st.error("No query found")

    banks = execute_query(query, fetch_all=True)
    bank_options = {name: bank_id for bank_id, name in banks}

    return bank_options


def roles_list(bank_id):
    query = get_query("Roles list", filename)
    if query is None:
        st.error("No query found")

    roles = execute_query(query, (bank_id,), fetch_all=True)
    role_options = {name: role_id for role_id, name in roles}

    return role_options


def branches_list(bank_id):
    query = get_query("Branches list", filename)
    if query is None:
        st.error("No query found")

    branches = execute_query(query, fetch_all=True)
    branch_options = {name: branch_id for branch_id, name in branches}

    return branch_options


def register_page():
    st.title("📝 Register")
    st.write("Please select your role:")

    if st.button("Customer"):
        st.session_state.page = "register_customer"
    if st.button("Employee"):
        st.session_state.page = "register_employee"

    if st.button("Back to Home"):
        st.session_state.page = "home"


def register_employee():
    st.write("📝 Registration for an employee ")

    bank_options = banks_list()
    selected_bank_name = st.selectbox("Select your Bank", list(bank_options.keys()))

    if selected_bank_name:
        selected_bank_id = bank_options[selected_bank_name]

        role_options = roles_list(selected_bank_id)
        selected_role_name = st.selectbox("Select your role", list(role_options.keys()))
        selected_role_id = int(role_options[selected_role_name])

        if selected_role_name:
            first_name = st.text_input("First Name")
            middle_name = st.text_input("Middle Name")
            last_name = st.text_input("Last Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone", value="+374")

            if st.button("Register"):
                Logic.Registration.register_employee(first_name, middle_name, last_name, selected_role_name, phone, email, selected_role_id)

    if st.button("Back to registration"):
        st.session_state.page = "registration"


def register_customer():
    st.write("📝 Registration for a customer ")

    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))
    phone = st.text_input("Phone number", value="+374")
    email = st.text_input("Email")
    address = st.text_input("Address")

    bank_options = banks_list()
    selected_bank_name = st.selectbox("Select your Bank", list(bank_options.keys()))
    selected_bank_id = bank_options[selected_bank_name]

    if st.button("Register"):
        Logic.Registration.register_customer(first_name, middle_name, last_name, dob, email, address, phone,
                                             selected_bank_id)
    if st.button("Back to registration"):
        st.session_state.page = "registration"