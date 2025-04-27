from streamlit import cache_resource
import psycopg2

#TODO: Change connection parameters
@cache_resource
def get_connection():
    conn = psycopg2.connect(
        dbname="YOURDBNAME",
        user="postgres",
        password="PASSWORD",
        host="localhost",
        port="5432"
    )
    return conn

def read_file(filename):
    queries = {}

    with open(filename, "r") as file:
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

def get_query(tag, filename):
    queries = read_file(filename)
    return queries.get(tag)


def execute_query(query, params=None, fetch_all=False, return_row=False):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute(query, params)
        if cursor.description:
            if fetch_all:
                return cursor.fetchall()
            else:
                result = cursor.fetchone()
                if result:
                    if return_row:
                        return result
                    else:
                        return result[0]
                else:
                    return None
    conn.commit()
    return None