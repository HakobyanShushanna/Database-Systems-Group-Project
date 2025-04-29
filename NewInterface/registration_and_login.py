import streamlit as st

from BackEnd.login_logic import login_admin
from BackEnd.registration_logic import register_admin

def register_login():
    st.title("📝 Registration and login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        success = register_admin(username, password)
        if not success[0]:
            st.warning(success[1])
        else:
            st.session_state.page = "profile"
            return
    if st.button("Login"):
        success = login_admin(username, password)
        if not success[0]:
            st.warning(success[1])
        else:
            st.session_state.page = "profile"
            return

    if st.button("Back to Home"):
        st.session_state.page = "home"