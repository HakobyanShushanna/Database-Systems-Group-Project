from BackEnd.common_functions import get_query, execute_query, add_person
from datetime import datetime
from static_variables import crud, search_filter, report
from config import get_connection


def __format_person(person):
    return f"{person[1]} {person[2] if person[2] else ""} {person[3]} (ID : {person[0]})"


def __format_transaction(transaction):
    return f"Date: {transaction[6]} | ${transaction[3]} (ID: {transaction[0]})"


def __format_loan(loan):
    return f"Amount: {loan[3]} | Due: {loan[5]} | Interest rate: {loan[7]} | Repaid amount: {loan[12]} (Id: {loan[0]})"


def add_employee(first_name: str, middle_name: str, last_name: str, role: str, phone: str, email: str, position_id: int, branch_id: int):
    conn = get_connection()
    try:
        employee_id = add_person(first_name, middle_name, last_name, role, phone, email, conn=conn)
        if not employee_id:
            conn.rollback()
            return False, "Failed to insert person"

        employee_query = get_query("Add employee", crud)
        if not employee_query:
            conn.rollback()
            return False, "Employee query not found"

        params = (employee_id, position_id)
        success = execute_query(employee_query, params, conn=conn)
        if not success:
            conn.rollback()
            return False, "Something went wrong while adding the employee"

        branch_employee_query = get_query("Add branch_employee", crud)
        if not branch_employee_query:
            conn.rollback()
            return False, "Employee & Branch query not found"

        params = (branch_id, employee_id[0])
        success = execute_query(branch_employee_query, params, conn=conn)
        if success:
            conn.commit()
            return True, "Employee added successfully"

        conn.rollback()
        return False, "Something went wrong while connecting the employee to the branch"

    except Exception as e:
        conn.rollback()
        return False, f"Unexpected error: {e}"

    finally:
        conn.close()


def add_customer(first_name, middle_name, last_name, role, phone, email, date_of_birth, address, bank_id):
    conn = get_connection()
    try:
        customer_id = add_person(first_name, middle_name, last_name, role, phone, email, conn=conn)
        if not customer_id:
            conn.rollback()
            return False, "Failed to insert person"

        customer_query = get_query("Add customer", crud)
        if not customer_query:
            conn.rollback()
            return False, "Customer query not found"

        print(f"[DEBUG] customer_query: {customer_query}")
        params = (customer_id, date_of_birth, address, bank_id)
        success = execute_query(customer_query, params, conn=conn)

        if success:
            conn.commit()
            return True, "Customer added successfully"

        conn.rollback()
        return False, "Something went wrong while adding the Customer"
    except Exception as e:
        conn.rollback()
        return False, f"Unexpected error: {e}"
    finally:
        conn.close()


def add_activity(employee_id:int, action:str, ip_address:str):
    query = get_query("Add audit_log", crud)

    if not query:
        return False, "Query Add audit_log does not exist"

    params = (employee_id, action, datetime.now(), ip_address)
    result = execute_query(query, params)

    if result:
        return result, "Action added successfully"
    return result, "Something went wrong while adding an action"


def add_transaction(sender_id:int, receiver_id:int, amount:float, description:str, type:str):
    query = get_query("Add transaction", crud)

    if not query:
        return False, "Add transaction query not found"

    params = (sender_id, receiver_id, amount, description, type, datetime.now())
    result = execute_query(query, params)

    if result:
        return result, "Transaction added successfully"
    return result, "Something went wrong while adding the transaction"


def add_loan(customer_id:int, loan_type:str, amount:float, issued_date:datetime, due_date:datetime, interest_rate:float, status:str):
    query = get_query("Add loan", crud)

    if not query:
        return False, "Add loan query not found"

    params = (customer_id, loan_type, amount, issued_date, due_date, datetime.now(), interest_rate, status)
    result = execute_query(query, params)

    if result:
        return result, "Loan added successfully"
    return result, "Something went wrong while adding the transaction"


# ==========================================================================================
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


def get_transaction(customer_id:int, operation:str):
    operation = operation.capitalize()
    query = get_query(operation, report)

    if not query:
        return False, f"{operation} query not found"

    params = (customer_id, )
    if operation == "Transactions":
        params = (customer_id, customer_id)

    transactions_list = execute_query(query, params, fetch_all=True)
    transactions_list = {__format_transaction(transaction) for transaction in transactions_list}

    print(F"[DEBUG] {type(transactions_list)}")
    print(F"[DEBUG] {transactions_list}")

    return True, transactions_list


def get_loan(customer_id):
    query = get_query("Loans", report)

    if not query:
        return False, "Loans query not found"

    loan_list = execute_query(query, (customer_id, ), fetch_all=True)

    loan_list = {__format_loan(loan) for loan in loan_list}

    return loan_list


# =================================================================================================
def get_number_transactions(customer_id:int, operation:str):
    operation = operation.lower()
    query = get_query(f"The number of {operation}", report)

    if not query:
        return False, f"The number of {operation} query not found"

    params = (customer_id, )
    if operation == "transactions":
        params = (customer_id, customer_id,)

    count = execute_query(query, params)

    return count


def get_number_loans(customer_id):
    query = get_query("The number of loans", report)

    if not query:
        return False, "The number of loans query not found"

    result = execute_query(query, (customer_id, ))

    return True, result


def get_loan_amount(customer_id):
    query = get_query("Total loan amount", report)

    if not query:
        return False, "Total loan amount query not found"

    result = execute_query(query, (customer_id, ))

    return True, result


def get_loan_repayment_amount(customer_id):
    query = get_query("Total loan repayment amount", report)

    if not query:
        return False, "Total loan repayment amount query not found"

    result = execute_query(query, (customer_id, ))

    return True, result