from pydoc import describe

import streamlit as st
import BackEnd.admin_operations_logic as admin_operations_logic
from BackEnd.admin_operations_logic import get_employees
from BackEnd.data_from_db import get_banks, get_branches, get_roles
from datetime import datetime

def profile():
    st.write("Available Operations:")

    if st.button("Customers List"):
        st.session_state.page = "all_customers"
    if st.button("Employees List"):
        st.session_state.page = "all_employees"


def all_customers():
    st.write("Customers list")

    if st.button("Add a customer"):
        st.session_state.page = "add_customer"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    customers_list = admin_operations_logic.get_customers()

    for customer in customers_list:
        st.write(customer)


def all_employees():
    st.write("Employees list")

    if st.button("Add an employee"):
        st.session_state.page = "add_employee"

    employees_list = admin_operations_logic.get_employees()

    for employee in employees_list:
        st.write(employee)


def add_employee():
    st.title("📝 Add an Employee")

    bank_options = get_banks()
    selected_bank_name = st.selectbox("Bank", list(bank_options.keys()))

    if selected_bank_name:
        selected_bank_id = bank_options[selected_bank_name]

        branch_options = get_branches(selected_bank_id)
        selected_branch_name = st.selectbox("Branch", list(branch_options.keys()))
        selected_branch_id = branch_options[selected_branch_name]

        role_options = get_roles(selected_bank_id)
        selected_role_name = st.selectbox("Role", list(role_options.keys()))
        selected_role_id = role_options[selected_role_name]

        first_name = st.text_input("First Name")
        middle_name = st.text_input("Middle Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone", value="+374")

        if st.button("Register"):
            result = admin_operations_logic.add_employee(first_name, middle_name, last_name, selected_role_name, phone, email, selected_role_id, selected_branch_id)
            if result[0]:
                st.success(result[1])
                st.session_state.page = "success"
            else:
                st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_customer():
    st.title("📝 Add a Customer")

    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))
    phone = st.text_input("Phone Number", value="+374")
    email = st.text_input("Email")
    address = st.text_input("Address")

    bank_options = get_banks()
    selected_bank_name = st.selectbox("Bank", list(bank_options.keys()))
    selected_bank_id = bank_options[selected_bank_name]

    if st.button("Register"):
        result = admin_operations_logic.add_customer(first_name, middle_name, last_name, "customer", phone, email, dob, address, selected_bank_id)
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_activity():
    st.write("Add an Activity:")

    employee_options = get_employees()
    selected_employee = st.selectbox("Employee", list(employee_options.keys()))
    selected_employee_id = employee_options[selected_employee]

    action = st.text_input("Activity")
    ip_address = st.text_input("IP address")

    if st.button("Add"):
        result = admin_operations_logic.add_activity(selected_employee_id, action, ip_address)
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_transaction():
    st.write("Add a Transaction:")

    customers =  admin_operations_logic.get_customers()
    selected_sender = st.selectbox("Sender", list(customers.keys()))
    selected_sender_id = customers[selected_sender]

    selected_receiver = st.selectbox("Sender", list(customers.keys()))
    selected_receiver_id = customers[selected_receiver]

    amount = st.number_input("Amount", min_value=0.00)
    description = st.text_input("Description")
