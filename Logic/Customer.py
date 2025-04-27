from mako.testing.helpers import result_lines

from config import get_query, execute_query
import streamlit as st

filename = "Sql/Report.sql"

def get_deposits(id, number:bool = True):
    query = get_query("Deposits", filename)
    if number:
        query = get_query("The number of deposits", filename)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id,), not number)

    return result


def get_withdrawals(id, number:bool = True):
    query = get_query("Withdrawals", filename)
    if number:
        query = get_query("The number of withdrawals", filename)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id,), not number)

    return result


def get_transactions(id, number:bool = True):
    query = get_query("Transactions", filename)
    if number:
        query = get_query("The number of transactions", filename)

    if query is None:
        st.error("Query does not exist")
        return

    result = execute_query(query, (id, id,), not number)
    return result


def get_repayments(id, number:bool = True):
    query = get_query("Repayments", filename)
    if number:
        query = get_query("Total amount repaid", filename)

    if query is None:
        st.error("No query found")
        return

    result = execute_query(query, (id, ), not number)
    return result


def get_remining_balance(id):
    query = get_query("Remaining balance", filename)

    if query is None:
        st.error("Query not found")
        return

    result = execute_query(query, (id, ))
    return result


def get_loans(id, number:bool = True):
    query = get_query("Loans", filename)
    if number:
        query = get_query("Total loan amount", filename)

    if query is None:
        st.error("Query not found")
        return

    result = execute_query(query, (id, ), not number)
    return result

def get_cards(id):
    query = get_query("Cards", filename)

    if query is None:
        st.error("No Query found")
        return

    result = execute_query(query, (id, ), fetch_all=True)


def get_accounts(id):
    query = get_query("Accounts", filename)

    if query is None:
        st.error("No Query found")
        return

    result = execute_query(query, (id,), fetch_all=True)
