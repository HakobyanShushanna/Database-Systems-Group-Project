import streamlit as st
from Logic.Login import login_user

def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if not username or not password:
            st.error("Please fill in all fields.")
            return

        user, role = login_user(username, password)

        if user is None:
            st.error(role)
            return

        st.session_state.user = user

        if role == "customer":
            st.session_state.page = "my_profile"
        elif role == "employee":
            st.session_state.page = "my_profile_employee"

        st.rerun()