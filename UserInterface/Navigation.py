import streamlit as st
from UserInterface.Main import main_page
import UserInterface.Registration
import UserInterface.Login

def navigation():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if st.session_state.page == "home":
        main_page()
    elif st.session_state.page == "login":
        UserInterface.Login.login_page()
    elif st.session_state.page == "registration":
        UserInterface.Registration.register_page()
    elif st.session_state.page == "register_customer":
        UserInterface.Registration.register_customer()
    elif st.session_state.page == "register_employee":
        UserInterface.Registration.register_employee()