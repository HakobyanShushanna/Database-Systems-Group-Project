import streamlit as st
from NewInterface.registration_and_login import register_login
import NewInterface.admin_operations as admin_operations


def navigation():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.session_state.page == "home":
        home()
    if st.session_state.page == "success":
        success()
    elif st.session_state.page == "login_or_register":
        register_login()
    elif st.session_state.page == "profile":
        admin_operations.profile()
    elif st.session_state.page == "all_customers":
        admin_operations.all_customers()
    elif st.session_state.page == "all_employees":
        admin_operations.all_employees()
    elif st.session_state.page == "add_customer":
        admin_operations.add_customer()
    elif st.session_state.page == "add_employee":
        admin_operations.add_employee()
    elif st.session_state.page == "add_activity":
        admin_operations.add_activity()


def home():
    st.title("🏦 Welcome to the Banking System")
    st.write("Please select an option:")

    if st.button("Login or Register"):
        st.session_state.page = "login_or_register"


def success():
    st.write("Success")