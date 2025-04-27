import streamlit as st

import Logic.Customer
from Logic.Customer import get_deposits, get_withdrawals, get_transactions, get_repayments, get_remining_balance, get_loans
from Models.customer_model import CustomerModel
from Models.card_model import CardModel
from Models.account_model import AccountModel
from Models.transaction_model import TransactionModel


def profile(customer: CustomerModel):
    number_of_deposits = get_deposits(customer.id)
    number_of_withdrawals = get_withdrawals(customer.id)
    number_of_transactions = get_transactions(customer.id)
    repaid = get_repayments(customer.id)
    to_repay = get_remining_balance(customer.id)
    loan_amount = get_loans(customer.id)

    st.title(f"🏦 Welcome, {customer.first_name} {customer.last_name}!")

    st.write("About you:")
    st.write(f"Email: {customer.email}")
    st.write(f"Phone: {customer.phone}")
    st.write(f"Bank: {customer.bank}")
    st.write(f"Date of Birth: {customer.date_of_birth}")
    st.write(f"Address: {customer.address}")

    st.write("================ REPORT ================")

    st.write(f"Number of Deposits: {number_of_deposits}")
    st.write(f"Number of Withdrawals: {number_of_withdrawals}")
    st.write(f"Number of Transactions: {number_of_transactions}")
    st.write(f"Total repayment: {repaid}")
    st.write(f"Remined to Repay: {to_repay}")
    st.write(f"Total Loan Amount: {loan_amount}")

    if st.button("My Accounts"):
        st.session_state.page = "accounts"
    if st.button("My cards"):
        st.session_state.page = "cards"
    if st.button("Deposits"):
        st.session_state.page = "deposits"
    if st.button("Withdrawals"):
        st.session_state.page = "withdrawals"
    if st.button("All transactions"):
        st.session_state.page = "transactions"
    if st.button("Logout"):
        st.session_state.page = "logout"
    if st.button("Delete"):
        st.session_state.page = "delete"


def cards(card_lst: list[CardModel]):
    st.write("Your available cards:")

    for card in card_lst:
        st.write("======================================")
        st.write(card.card_number)
        st.write(card.card_type)
        st.write(card.expiry_date)
        st.write(card.cvv)
        st.write(f"Status: {card.status}")
        st.write("======================================")

    if st.button("Back to my profile"):
        st.session_state.page = "my_profile"


def accounts(account_lst: list[AccountModel]):
    st.write("Your available accounts:")

    if st.button("Add a new Account"):
        st.session_state.page = "add_account"

    for account in account_lst:
        st.write("======================================")
        st.write(account.account_type)
        st.write(account.bank)
        st.write(account.created_at)
        st.write(account.status)
        st.write("======================================")

    if st.button("Back to my profile"):
        st.session_state.page = "my_profile"


def withdrawals(withdrawal_lst: list[TransactionModel]):
    st.write("Your withdrawals:")

    if st.button("Add a new Withdrawal"):
        st.session_state.page = "add_withdrawal"

    for withdrawal in withdrawal_lst:
        st.write("======================================")
        st.write(f"Type: {withdrawal.type}")
        st.write(f"Amount: {withdrawal.amount}")
        st.write(f"Receiver: {withdrawal.receiver}")
        st.write(f"Description: {withdrawal.description}")
        st.write(f"Date: {withdrawal.transaction_date}")
        st.write("======================================")

    if st.button("Back to my profile"):
        st.session_state.page = "my_profile"


def deposits(deposit_lst: list[TransactionModel]):
    st.write("Your deposits:")

    if st.button("Add a new Deposit"):
        st.session_state.page = "add_deposit"

    for deposit in deposit_lst:
        st.write("======================================")
        st.write(f"Type: {deposit.type}")
        st.write(f"Amount: {deposit.amount}")
        st.write(f"Sender: {deposit.sender}")
        st.write(f"Description: {deposit.description}")
        st.write(f"Date: {deposit.transaction_date}")
        st.write("======================================")

    if st.button("Back to my profile"):
        st.session_state.page = "my_profile"


def transactions(transaction_lst: list[TransactionModel]):
    st.write("Your transactions:")

    for transaction in transaction_lst:
        st.write("======================================")
        st.write(f"Type: {transaction.type}")
        st.write(f"Amount: {transaction.amount}")
        st.write(f"Sender: {transaction.sender}")
        st.write(f"Receiver: {transaction.receiver}")
        st.write(f"Description: {transaction.description}")
        st.write(f"Date: {transaction.transaction_date}")
        st.write("======================================")

    if st.button("Back to my profile"):
        st.session_state.page = "my_profile"

def add_account():
    st.title("➕ Add a New Account")

    account_type = st.selectbox("Select Account Type", ["Checking", "Savings", "Business", "Loan"])
    bank = st.text_input("Bank Name")
    initial_balance = st.number_input("Initial Balance", min_value=0.0)

    if st.button("Submit New Account"):
        success = Logic.Customer.add_account(account_type, bank, initial_balance)
        if success:
            st.success("Account added successfully.")
            st.session_state.page = "accounts"
        else:
            st.error("Failed to add account. Try again.")


def add_withdrawal():
    st.title("➖ Make a Withdrawal")

    amount = st.number_input("Withdrawal Amount", min_value=0.0)
    receiver = st.text_input("Receiver")
    description = st.text_area("Description")

    if st.button("Submit Withdrawal"):
        success = Logic.Customer.add_withdrawal(amount, receiver, description)
        if success:
            st.success("Withdrawal added successfully.")
            st.session_state.page = "withdrawals"
        else:
            st.error("Failed to add withdrawal. Try again.")


def add_deposit():
    st.title("➕ Make a Deposit")

    amount = st.number_input("Deposit Amount", min_value=0.0)
    sender = st.text_input("Sender")
    description = st.text_area("Description")

    if st.button("Submit Deposit"):
        success = Logic.Customer.add_deposit(amount, sender, description)
        if success:
            st.success("Deposit added successfully.")
            st.session_state.page = "deposits"
        else:
            st.error("Failed to add deposit. Try again.")


def logout():
    st.title("👋 Logout")

    st.success("You have been logged out successfully.")
    st.session_state.clear()
    st.session_state.page = "login"


def delete():
    st.title("⚠️ Delete Account")

    st.warning("Are you sure you want to delete your account? This action cannot be undone.")

    if st.button("Yes, delete my account"):

        st.success("Your account has been deleted.")
        st.session_state.clear()
        st.session_state.page = "register"

    if st.button("No, go back to profile"):
        st.session_state.page = "my_profile"
