import streamlit as st

def login_page():
    st.title("🔐 Login")
    st.write("Please select your role:")

    if st.button("User"):
        st.session_state.page = "login_user"
    if st.button("Employee"):
        st.session_state.page = "login_employee"

    if st.button("Back to Home"):
        st.session_state.page = "home"