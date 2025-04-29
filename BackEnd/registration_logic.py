from BackEnd.common_functions import encrypt, get_query, execute_query
from static_variables import shift, crud


def register_admin(username:str, password:str):
    admin_query = get_query("Add login", crud)

    if not admin_query:
        return False, "Login query not found"

    password_hash = encrypt(password, shift)
    params = (username, password_hash, )

    success = execute_query(admin_query, params)

    if success:
        return True, "Admin registered successfully"
    return False, "Something went wrong while registering an Admin"