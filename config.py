from streamlit import cache_resource
import psycopg2

#TODO: Change connection parameters
def get_connection():
    conn = psycopg2.connect(
        dbname="YOURDBNAME",
        user="postgres",
        password="YOURPASSWORD",
        host="localhost",
        port="5432"
    )
    return conn
