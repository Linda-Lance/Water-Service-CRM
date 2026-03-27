import pandas as pd
from db import get_connection

def generate_services_for_selected_date(selected_date):

    conn = get_connection()

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

    # ✅ Ensure proper datetime conversion
    df["Service Date"] = pd.to_datetime(
        df["Service Date"], errors="coerce", dayfirst=True
    )

    df["Next Service Date"] = pd.to_datetime(
        df["Next Service Date"], errors="coerce", dayfirst=True
    )

    # Remove invalid dates
    df = df.dropna(subset=["Service Date"])

    # ✅ Filter
    result = df[df["Service Date"].dt.date == selected_date]

    if result.empty:
        return "No services found for this date."

    result = result.copy()
    

    # ✅ FORMAT HERE (final step)
    result["Service Date"] = result["Service Date"].dt.strftime("%d-%m-%Y")
    result["Next Service Date"] = result["Next Service Date"].dt.strftime("%d-%m-%Y")

    result["Service Date"] = result["Service Date"].astype(str)
    result["Next Service Date"] = result["Next Service Date"].astype(str)

    return result