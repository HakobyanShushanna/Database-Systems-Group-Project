from config import get_query, execute_query
import streamlit as st

filename = "Sql/Report.sql"

def get_number_of_employees(branch_id):
    query = get_query("Number of employees by branch", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (branch_id,))


def get_number_of_customers(bank_id):
    query = get_query("Number of customers by bank", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (bank_id,))


def get_number_of_accounts(bank_id):
    query = get_query("Number of accounts by bank", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (bank_id,))


def get_number_of_cards():
    query = get_query("Number of cards", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query)


def get_employees_by_branch(branch_id):
    query = get_query("Employees by branch", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (branch_id,), fetch_all=True)


def get_customers_by_bank(bank_id):
    query = get_query("Customers by bank", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (bank_id,), fetch_all=True)


def get_accounts_by_bank(bank_id):
    query = get_query("Accounts by bank", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, (bank_id,), fetch_all=True)


def get_all_cards():
    query = get_query("Cards", filename)

    if query is None:
        st.error("Query does not exist")
        return

    return execute_query(query, fetch_all=True)