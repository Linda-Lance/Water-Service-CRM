import streamlit as st
from datetime import date

from auth import login, check_auth
from ai_engine import search_customer, search_by_product, search_by_location
from scheduler import generate_services_for_selected_date
from db import get_connection

st.set_page_config(page_title="Water CRM", layout="wide")

# LOGIN
login()
if not check_auth():
    st.stop()

st.title("💧 Water Service CRM Dashboard")

# ---------------- SEARCH CUSTOMER ----------------
st.header("🔎 Search Customer")

search_name = st.text_input("Search Name")
search_phone = st.text_input("Search Phone")

if st.button("Search Customer"):
    result = search_customer(search_name.strip(), search_phone.strip())

    if result.empty:
        st.warning("No records found")
    else:
        st.dataframe(result, use_container_width=True)


# ---------------- PRODUCT SEARCH ----------------
st.header("📦 Search by Product")

product_search = st.text_input("Enter Product Model")

if st.button("Find Product Customers"):
    result = search_by_product(product_search)

    if result.empty:
        st.warning("No customers found")
    else:
        st.dataframe(result)


# ---------------- LOCATION SEARCH ----------------
st.header("📍 Search by Location")

location = st.text_input("Enter Location")

if st.button("Find Customers in Location"):
    result = search_by_location(location)

    if result.empty:
        st.warning("No customers found")
    else:
        st.dataframe(result)


# ---------------- DUE SERVICES ----------------
st.header("📅 Due Services")

selected_date = st.date_input(
    "Select Service Date",
    value=date.today(),
    format="DD-MM-YYYY")
final_date = selected_date.strftime("%d-%m-%y")

if st.button("Find Services"):
    result = generate_services_for_selected_date(selected_date)

    if isinstance(result, str):
        st.warning(result)
    elif result.empty:
        st.warning("No services found for this date")
    else:
        st.dataframe(result)

# ---------------- AUTO TODAY ALERT ----------------
st.header("⚠️ Today’s Due Services")

today_result = generate_services_for_selected_date(date.today())

if isinstance(today_result, str):
    st.warning(today_result)

elif today_result.empty:
    st.success("No services today 🎉")

else:
    st.dataframe(today_result, use_container_width=True)