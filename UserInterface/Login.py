import streamlit as st
from Logic.Login import login_user
from Logic.ceasar import encrypt, decrypt


def login_page():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        encrypted_password = encrypt(password, 3)
        user = login_user(username, encrypted_password)

        if user:
            st.session_state.user = user
            st.session_state.page = "my_profile"
            st.rerun()
        else:
            st.error("Invalid login credentials, please try again.")

    if st.button("Back to Home"):
        st.session_state.page = "home"
        st.rerun()
