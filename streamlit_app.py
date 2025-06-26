import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Age + Voting Eligibility", page_icon="🗳️")
st.title("🧮 Age Calculator & Voting Checker")

birth_year = st.number_input("Enter your birth year (e.g. 2005)", min_value=1900, max_value=2100, step=1)

if st.button("Check"):
    current_year = datetime.now().year
    age = current_year - birth_year

    st.success(f"You are {age} years old.")

    if age >= 18:
        st.info("✅ You can vote.")
    else:
        st.warning("❌ You are a minor, so you cannot vote yet.")

    st.caption("Thanks for trying.")
