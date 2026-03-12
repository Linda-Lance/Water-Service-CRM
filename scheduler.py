import sqlite3
import pandas as pd

DB = "water_service.db"

def generate_services_for_selected_date(selected_date):

    conn = sqlite3.connect(DB)

    query = """
    SELECT 
        c.[Customer Name],
        c.[Phone Number],
        c.[Address],
        c.[Product],
        s.[Service Date],
        s.[Service Type],
        s.[Technician],
        s.[Next Service Date],
        s.[Remarks]
    FROM services s
    JOIN customers c
    ON s.[Customer ID] = c.[Customer ID]
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    df["Service Date"] = pd.to_datetime(df["Service Date"], dayfirst=True)

    result = df[df["Service Date"].dt.date == selected_date]

    if result.empty:
        return "No services found for this date."

    result["Service Date"] = result["Service Date"].dt.strftime("%d-%m-%Y")
    result["Next Service Date"] = pd.to_datetime(result["Next Service Date"], dayfirst=True).dt.strftime("%d-%m-%Y")

    return result