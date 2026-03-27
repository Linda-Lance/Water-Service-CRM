import pandas as pd
from db import get_connection

# Search Customer
def search_customer(name=None, phone=None):

    conn = get_connection()

    query = """
    SELECT DISTINCT
        c.[Customer Name],
        c.[Phone Number],
        c.[Address],
        c.[Product],
        s.[Service Date],
        s.[Service Type],
        s.[Technician],
        s.[Next Service Date]
    FROM customers c
    LEFT JOIN services s
    ON c.[Customer ID] = s.[Customer ID]
    """

    conditions = []
    params = []

    if name:
        conditions.append("LOWER(c.[Customer Name]) LIKE LOWER(?)")
        params.append(f"%{name}%")

    if phone:
        conditions.append("c.[Phone Number] = ?")
        params.append(phone)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    df = pd.read_sql_query(query, conn, params=params)
    conn.close()

    return df


# Search by Product
def search_by_product(product):

    conn = get_connection()

    query = """
    SELECT 
        [Customer Name],
        [Phone Number],
        [Address],
        [Product]
    FROM customers
    WHERE LOWER([Product]) LIKE LOWER(?)
    """

    df = pd.read_sql_query(query, conn, params=(f"%{product}%",))
    conn.close()

    return df


# Search by Location
def search_by_location(location):

    conn = get_connection()

    query = """
    SELECT 
        [Customer Name],
        [Phone Number],
        [Address],
        [Product]
    FROM customers
    WHERE LOWER([Address]) LIKE LOWER(?)
    """

    df = pd.read_sql_query(query, conn, params=(f"%{location}%",))
    conn.close()

    return df