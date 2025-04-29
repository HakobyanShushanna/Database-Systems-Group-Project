from streamlit import cache_resource
import psycopg2

#TODO: Change connection parameters
def get_connection():
    conn = psycopg2.connect(
        dbname="BankingSystem",
        user="postgres",
        password="Tumo4227!",
        host="localhost",
        port="5432"
    )
    return conn