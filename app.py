import streamlit as st
from bank import BankAccount

st.title("💰 Simple Banking App")

# Create a single account for this session
if 'account' not in st.session_state:
    st.session_state.account = BankAccount()

# Show current balance
st.subheader("Current Balance:")
st.write(f"${st.session_state.account.get_balance():.2f}")

# Deposit
st.subheader("Deposit Money")
deposit_amount = st.number_input("Amount to deposit", min_value=0.0, step=10.0)
if st.button("Deposit"):
    try:
        st.session_state.account.deposit(deposit_amount)
        st.success(f"Deposited ${deposit_amount:.2f}")
    except ValueError as e:
        st.error(str(e))

# Withdraw
st.subheader("Withdraw Money")
withdraw_amount = st.number_input("Amount to withdraw", min_value=0.0, step=10.0, key="withdraw_input")
if st.button("Withdraw"):
    try:
        st.session_state.account.withdraw(withdraw_amount)
        st.success(f"Withdrew ${withdraw_amount:.2f}")
    except ValueError as e:
        st.error(str(e))
