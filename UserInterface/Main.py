import streamlit as st

def main_page():
    st.title("🏦 Welcome to Streamlit Bank")
    st.write("Please select an option:")

    if st.button("Login"):
        st.session_state.page = "login"
    if st.button("Register"):
        st.session_state.page = "registration"