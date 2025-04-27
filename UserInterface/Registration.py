import streamlit as st
import Logic.Registration
from datetime import datetime
from Logic.Registration import banks_list, roles_list

def register_page():
    st.title("📝 Register")
    st.write("Please select your role:")

    if st.button("Customer"):
        st.session_state.page = "register_customer"
    if st.button("Employee"):
        st.session_state.page = "register_employee"
    if st.button("Back to Home"):
        st.session_state.page = "home"


def register_employee():
    st.title("📝 Employee Registration")

    bank_options = banks_list()
    selected_bank_name = st.selectbox("Select your Bank", list(bank_options.keys()))

    if selected_bank_name:
        selected_bank_id = bank_options[selected_bank_name]
        role_options = roles_list(selected_bank_id)
        selected_role_name = st.selectbox("Select your Role", list(role_options.keys()))
        selected_role_id = role_options[selected_role_name]

        first_name = st.text_input("First Name")
        middle_name = st.text_input("Middle Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone", value="+374")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Register"):
            user, error = Logic.Registration.register_employee(
                first_name, middle_name, last_name, selected_role_name, phone, email, password, username, selected_role_id
            )
            if user:
                st.session_state.user = user
                st.session_state.page = "my_profile_employee"
                st.rerun()
            else:
                st.error(error)

    if st.button("Back to Registration"):
        st.session_state.page = "registration"


def register_customer():
    st.title("📝 Customer Registration")

    first_name = st.text_input("First Name")
    middle_name = st.text_input("Middle Name")
    last_name = st.text_input("Last Name")
    dob = st.date_input("Date of Birth", min_value=datetime(1900, 1, 1))
    phone = st.text_input("Phone Number", value="+374")
    email = st.text_input("Email")
    address = st.text_input("Address")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    bank_options = banks_list()
    selected_bank_name = st.selectbox("Select your Bank", list(bank_options.keys()))
    selected_bank_id = bank_options[selected_bank_name]

    if st.button("Register"):
        user, error = Logic.Registration.register_customer(
            first_name, middle_name, last_name, dob, email, address, phone, password, username, selected_bank_id
        )
        if user:
            st.session_state.user = user
            st.session_state.page = "my_profile"
            st.rerun()
        else:
            st.error(error)

    if st.button("Back to Registration"):
        st.session_state.page = "registration"