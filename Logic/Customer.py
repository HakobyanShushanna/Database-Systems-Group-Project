from config import get_query, execute_query
import streamlit as st
from static_files import report, crud


def get_deposits(id, number:bool = True):
    query = get_query("Deposits", report)
    if number:
        query = get_query("The number of deposits", report)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id,), not number)

    return result


def get_withdrawals(id, number:bool = True):
    query = get_query("Withdrawals", report)
    if number:
        query = get_query("The number of withdrawals", report)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id,), not number)

    return result


def get_transactions(id, number:bool = True):
    query = get_query("Transactions", report)
    if number:
        query = get_query("The number of transactions", report)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id, id,), not number)
    return result


def get_repayments(id, number:bool = True):
    query = get_query("Repayments", report)
    if number:
        query = get_query("Total amount repaid", report)

    if query is None:
        st.error("No query found")
        return

    result = execute_query(query, (id, ), not number)
    return result


def get_remining_balance(id):
    query = get_query("Remaining balance", report)

    if query is None:
        st.error("Query not found")
        return

    result = execute_query(query, (id, ))
    return result


def get_loans(id, number:bool = True):
    query = get_query("Loans", report)
    if number:
        query = get_query("Total loan amount", report)

    if query is None:
        st.error("Query not found")
        return

    result = execute_query(query, (id, ), not number)
    return result

def get_cards(id):
    query = get_query("Cards", report)

    if query is None:
        st.error("No Query found")
        return

    result = execute_query(query, (id, ), fetch_all=True)


def get_accounts(id):
    query = get_query("Accounts", report)

    if query is None:
        st.error("No Query found")
        return

    result = execute_query(query, (id,), fetch_all=True)

def add_account(user_id, account_type, bank, initial_balance):
    query = get_query("Add account", crud)

    if query is None:
        st.error("Query does not exist")
        return

    params = (user_id, account_type, bank, initial_balance)
    execute_query(query, params)


def add_withdrawal(user_id, account_id, amount, receiver, description):
    query = get_query("Add withdrawal", crud)

    if query is None:
        st.error("Query does not exist")
        return

    params = (user_id, account_id, amount, receiver, description)
    execute_query(query, params)


def add_deposit(user_id, account_id, amount, sender, description):
    query = get_query("Add deposit", crud)

    if query is None:
        st.error("Query does not exist")
        return

    params = (user_id, account_id, amount, sender, description)
    execute_query(query, params)


def delete_account(account_id):
    query = get_query("Delete account", crud)

    if query is None:
        st.error("Query does not exist")
        return

    params = (account_id,)
    execute_query(query, params)