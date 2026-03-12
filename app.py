import streamlit as st
from datetime import date

from ai_engine import search_customer, search_by_product, search_by_location
from scheduler import generate_services_for_selected_date


st.title("💧 Water Service CRM Dashboard")

# CUSTOMER SEARCH
st.header("🔎 Search Customer")

name = st.text_input("Customer Name")
phone = st.text_input("Phone Number")

if st.button("Search Customer"):
    result = search_customer(name, phone)

    if result.empty:
        st.warning("No records found")
    else:
        st.dataframe(result)


# PRODUCT SEARCH
st.header("📦 Search by Product")

product = st.text_input("Enter Product Model")

if st.button("Find Product Customers"):
    result = search_by_product(product)

    if result.empty:
        st.warning("No customers found")
    else:
        st.dataframe(result)


# LOCATION SEARCH
st.header("📍 Search by Location")

location = st.text_input("Enter Location")

if st.button("Find Customers in Location"):
    result = search_by_location(location)

    if result.empty:
        st.warning("No customers found")
    else:
        st.dataframe(result)


# DUE SERVICES
st.header("📅 Due Services")

selected_date = st.date_input(
    "Select Service Date",
    value=date.today(),
    format="DD-MM-YYYY"
)

if st.button("Find Services Due"):

    result = generate_services_for_selected_date(selected_date)

    if isinstance(result, str):
        st.warning(result)
    else:
        st.dataframe(result)