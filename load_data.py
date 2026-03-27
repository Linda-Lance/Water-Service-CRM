import pandas as pd
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "water_service.db")

# Excel paths
customers_file = os.path.join(BASE_DIR, "data_record", "Customers.xlsx")
services_file = os.path.join(BASE_DIR, "data_record", "Services.xlsx")

# Load Excel
customers_df = pd.read_excel(customers_file)
services_df = pd.read_excel(services_file)

# Connect DB
conn = sqlite3.connect(db_path)

# Save to DB
customers_df.to_sql("customers", conn, if_exists="replace", index=False)
services_df.to_sql("services", conn, if_exists="replace", index=False)

conn.close()

print("✅ Data loaded successfully into database!")