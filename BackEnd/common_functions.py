from config import get_connection
from static_variables import crud
import re
import os

def __read_file(filename):
    queries = {}

    # Build absolute path to the Sql/ directory
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.normpath(os.path.join(base_dir, "..", "Sql", filename))

    with open(full_path, "r", encoding="utf-8") as file:
        content = file.read()

    parts = content.split("-- ")
    for part in parts:
        if not part.strip():
            continue

        lines = part.splitlines()
        tag = lines[0].strip()
        sql = " ".join(lines[1:]).strip()
        queries[tag] = sql

    return queries


def __format_phone(phone):
    phone = re.sub(r'\D', '', phone)
    if phone.startswith("0"):
        phone = phone[1:]
    if not phone.startswith("374"):
        phone = "374" + phone
    return "+" + phone


def get_query(tag, filename):
    queries = __read_file(filename)
    return queries.get(tag)


def execute_query(query, params=None, fetch_all=False, return_row=False):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description:
                if fetch_all:
                    return cursor.fetchall()
                else:
                    result = cursor.fetchone()
                    if result:
                        return result if return_row else result[0]
                    else:
                        return None
            else:
                conn.commit()
                return cursor.rowcount > 0
    except Exception as e:
        conn.rollback()
        print(f"Query failed: {e}")
        return False
    finally:
        conn.close()


def add_person(first_name:str, middle_name:str, last_name:str, role:str, phone:str, email:str):
    query = get_query("Add person", crud)

    if not query:
        return False

    phone = __format_phone(phone)
    params = (first_name, middle_name, last_name, role, phone, email,)

    result = execute_query(query, params)
    print(f"[DEBUG] Person insert result: {result}")

    return result if result else False


def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text