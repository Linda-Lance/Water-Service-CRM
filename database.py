import pandas as pd
import sqlite3

conn = sqlite3.connect("water_service.db")

customers = pd.read_excel("data/Customers.xlsx")
services = pd.read_excel("data/Services.xlsx")

customers.to_sql("customers", conn, if_exists="replace", index=False)
services.to_sql("services", conn, if_exists="replace", index=False)

conn.close()

print("Database recreated successfully")