import streamlit as st
import UserInterface.Registration
import UserInterface.Login
import UserInterface.Customer
from Logic.Customer import get_cards, get_accounts, get_deposits, get_withdrawals, get_transactions
from UserInterface.Main import main_page

def navigation():
    user = st.session_state.get('user', None)

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
    elif st.session_state.page == "my_profile" and user is not None:
        UserInterface.Customer.profile(user)
    elif st.session_state.page == "cards" and user is not None:
        card_lst = get_cards(user.id)
        UserInterface.Customer.cards(card_lst)
    elif st.session_state.page == "accounts" and user is not None:
        account_lst = get_accounts(user.id)
        UserInterface.Customer.cards(account_lst)
    elif st.session_state.page == "deposits":
        deposits_lst = get_deposits(user.id, False)
        UserInterface.Customer.deposits(deposits_lst)
    elif st.session_state.page == "withdrawals":
        withdrawals_lst = get_withdrawals(user.id, False)
        UserInterface.Customer.deposits(withdrawals_lst)
    elif st.session_state.page == "transactions":
        transactions_lst = get_transactions(user.id, False)
        UserInterface.Customer.deposits(transactions_lst)
    else:
        error_page()


def error_page():
    st.write("Coming Soon (or not)")
