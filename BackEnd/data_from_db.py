from static_variables import search_filter
from BackEnd.common_functions import get_query, execute_query

def get_banks():
    query = get_query("Banks list", search_filter)

    if not query:
        return {}

    banks = execute_query(query, fetch_all=True)

    return {name: bank_id for bank_id, name in banks}


def get_roles(bank_id:int):
    query = get_query("Roles list", search_filter)

    if not query:
        return {}

    roles = execute_query(query, (bank_id, ), fetch_all=True)

    return {name:role_id for role_id, name in roles}


def get_branches(bank_id:int):
    query = get_query("Branches list", search_filter)

    if not query:
        return {}

    branches = execute_query(query, (bank_id, ), fetch_all=True)

    return {name:branch_id for branch_id, name in branches}