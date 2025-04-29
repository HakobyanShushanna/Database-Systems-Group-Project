from BackEnd.common_functions import get_query, execute_query, encrypt
from static_variables import search_filter, shift


def login_admin(username: str, password: str):
    query = get_query("Login", search_filter)

    if not query:
        return False, "No Login search query exists"

    password_hash = encrypt(password, shift)
    params = (username, password_hash)
    success = execute_query(query, params)

    if success:
        return success, "Login successful"
    return success, "Incorrect username or password"