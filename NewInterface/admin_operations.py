import streamlit as st
from cloudinit.reporting.events import status

import BackEnd.admin_operations_logic as admin_operations_logic
from BackEnd.data_from_db import get_banks, get_branches, get_roles
from datetime import datetime

def profile():
    st.title("Available Operations")

    if st.button("Customers List"):
        st.session_state.page = "all_customers"
    if st.button("Employees List"):
        st.session_state.page = "all_employees"
    if st.button("Banks List"):
        st.session_state.page = "all_banks"
    if st.button("Branches List"):
        st.session_state.page = "all_branches"

    st.title("Customer related operations")
    customers = admin_operations_logic.get_customers()
    selected_customer_key = st.selectbox("Customer", list(customers.keys()))
    selected_customer_id = customers[selected_customer_key]

    if st.button("Transactions List") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "transactions_list"
    if st.button("Deposits List") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "deposits_list"
    if st.button("Withdrawals List") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "withdrawals_list"
    if st.button("Loan related") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "loan_related"
    if st.button("Cards") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "cards"
    if st.button("Accounts") and selected_customer_id:
        st.session_state.selected_customer_id = selected_customer_id
        st.session_state.page = "accounts"

    st.title("Employee related information")

    employees = admin_operations_logic.get_employees()
    selected_employee_key = st.selectbox("Employee", list(employees.keys()))
    selected_employee_id = employees[selected_employee_key]

    if st.button("Employee information") and selected_employee_id:
        st.session_state.selected_employee_id = selected_employee_id
        st.session_state.page = "employee_information"
    if st.button("Activity") and selected_employee_id:
        st.session_state.selected_employee_id = selected_employee_id
        st.session_state.page = "employee_activity"


def all_customers():
    st.title("Customers list")

    if st.button("Add a customer"):
        st.session_state.page = "add_customer"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    customers_list = admin_operations_logic.get_customers()

    for customer in customers_list:
        st.write(customer)


def all_employees():
    st.title("Employees list")

    if st.button("Add an employee"):
        st.session_state.page = "add_employee"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    employees_list = admin_operations_logic.get_employees()

    for employee in employees_list:
        st.write(employee)


def transactions_for_person(customer_id):
    st.title("Transactions for the user:")

    st.write(f"Number of transactions: {admin_operations_logic.get_number_transactions(customer_id, "transactions")}")

    if st.button("Add transaction:"):
        st.session_state.page = "add_transaction"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    transaction_list = admin_operations_logic.get_transaction(customer_id, "transactions")

    if not transaction_list[0]:
        st.warning(transaction_list[1])
        return

    if not len(transaction_list[1]):
        st.warning("No transactions for this user")
        return

    for transaction in transaction_list[1]:
        st.write(transaction)


def deposits_for_person(customer_id):
    st.title("Deposits for the user:")

    st.write(f"Number of transactions: {admin_operations_logic.get_number_transactions(customer_id, "deposits")}")

    if st.button("Add deposit:"):
        st.session_state.page = "add_deposit"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    deposit_list = admin_operations_logic.get_transaction(customer_id, "deposits")

    if not deposit_list[0]:
        st.warning(deposit_list[1])
        return

    if not len(deposit_list[1]):
        st.warning("No Deposits for this user")
        return

    for transaction in deposit_list[1]:
        st.write(transaction)


def withdrawals_for_person(customer_id):
    st.title("Withdrawals for the user:")

    st.write(f"Number of transactions: {admin_operations_logic.get_number_transactions(customer_id, "withdrawals")}")

    if st.button("Add Withdrawal:"):
        st.session_state.page = "add_withdrawal"

    if st.button("Back to profile"):
        st.session_state.page = "profile"

    deposit_list = admin_operations_logic.get_transaction(customer_id, "withdrawals")

    if not deposit_list[0]:
        st.warning(deposit_list[1])
        return

    if not len(deposit_list[1]):
        st.warning("No Deposits for this user")
        return

    for transaction in deposit_list[1]:
        st.write(transaction)


# ====================================================================================

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
    st.title("Add an Activity:")

    employee_options = admin_operations_logic.get_employees()
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
    st.title("Add a Transaction:")

    customers =  admin_operations_logic.get_customers()
    selected_sender = st.selectbox("Sender", list(customers.keys()), key = "sender_selectbox")
    selected_sender_id = customers[selected_sender]

    selected_receiver = st.selectbox("Receiver", list(customers.keys()), key = "receiver_selectbox")
    selected_receiver_id = customers[selected_receiver]

    amount = st.number_input("Amount", min_value=0.00)
    description = st.text_input("Description")

    if st.button("Add transaction"):
        result = admin_operations_logic.add_transaction(selected_sender_id, selected_receiver_id, amount, description, "transaction")
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_deposit(receiver_id):
    st.title("Add a Deposit:")

    customers =  admin_operations_logic.get_customers()
    selected_sender = st.selectbox("Sender", list(customers.keys()))
    selected_sender_id = customers[selected_sender]

    amount = st.number_input("Amount", min_value=0.00)
    description = st.text_input("Description")

    if st.button("Add transaction"):
        result = admin_operations_logic.add_transaction(selected_sender_id, receiver_id, amount, description, "deposit")
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_withdrawal(sender_id):
    st.title("Add a Deposit:")

    customers =  admin_operations_logic.get_customers()
    selected_receiver = st.selectbox("Sender", list(customers.keys()))
    selected_receiver_id = customers[selected_receiver]

    amount = st.number_input("Amount", min_value=0.00)
    description = st.text_input("Description")

    if st.button("Add transaction"):
        result = admin_operations_logic.add_transaction(sender_id, selected_receiver_id, amount, description, "withdrawal")
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


def add_loan(customer_id):
    st.title("Add loan for the user")

    loan_type = st.text_input("Type")
    amount = st.number_input("Amount", min_value=0.00)

    issued_date = st.date_input("Issued date", min_value=datetime.now())
    due_date = st.date_input("Due date", min_value=datetime.now())

    interest_rate = st.date_input("Interest rate", min_value=0.00)

    status = st.selectbox("Status", ('pending','active','closed','defaulted'))

    if st.button("Add loan"):
        result = admin_operations_logic.add_loan(customer_id, loan_type, amount, issued_date, due_date, interest_rate, status)
        if result[0]:
            st.success(result[1])
        else:
            st.warning(result[1])

    if st.button("Back to Profile"):
        st.session_state.page = "profile"


# ==================================================================================================================================
def loan_information(customer_id):
    st.title("Loan information")

    n_loans = admin_operations_logic.get_number_loans(customer_id)
    sum_loans = admin_operations_logic.get_loan_amount(customer_id)
    sum_repayments = admin_operations_logic.get_loan_repayment_amount(customer_id)

    st.write(f"The number of loans: {n_loans[1] if n_loans and n_loans[0] else 0}")
    st.write(f"The total amount: {sum_loans[1] if sum_loans and sum_loans[0] else 0}")
    st.write(f"Total amount repaid: {sum_repayments[1] if sum_repayments and sum_repayments[0] else 0}")

    if st.button("Add loan"):
        st.session_state.page = "add_loan"

    if st.button("Back to Profile"):
        st.session_state.page = "profile"

    loan_list = admin_operations_logic.get_loan(customer_id)

    for loan in loan_list:
        st.write(loan)