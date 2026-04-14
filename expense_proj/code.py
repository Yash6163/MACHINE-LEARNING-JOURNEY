import streamlit as st
import pandas as pd
from datetime import date
import os

st.title(" Personal Expense Tracker")
st.popover("CLICKJ")
# Load or create CSV
if os.path.exists("expenses.csv"):
    df = pd.read_csv("expenses.csv")
else:
    df = pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])

# Form to add new eXpense
st.header("Add New Expense")
with st.form("expense_form"):
    expense_date = st.date_input("Date", date.today())
    category = st.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.0, format="%.2f")
    notes = st.text_input("Notes (optional)")
    submitted = st.form_submit_button("Add Expense")
    
    if submitted:
        new_expense = {"Date": expense_date, "Category": category, "Amount": amount, "Notes": notes}
        df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
        df.to_csv("expenses.csv", index=False)
        st.success("Expense added!")

# Show expenses
st.header("All Expenses")
st.dataframe(df)

# Summary
st.header("Summary")
total = df["Amount"].sum()
st.write(f"**Total Spent:** ₹{total:.2f}")

by_category = df.groupby("Category")["Amount"].sum()
st.bar_chart(by_category)


