import streamlit as st

def add_menu():
    st.title("📝 Add an Employee or Customer")
    st.write("Please select the role you want to add:")

    if st.button("Customer"):
        st.session_state.page = "add_customer"
    if st.button("Employee"):
        st.session_state.page = "add_employee"
    if st.button("Back to Home"):
        st.session_state.page = "home"