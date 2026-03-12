import sqlite3
import pandas as pd

DB = "water_service.db"


# Search by Name + Phone
def search_customer(name=None, phone=None):

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
        conditions.append("c.[Phone Number] LIKE ?")
        params.append(f"%{phone}%")

    if conditions:
        query += " WHERE " + " OR ".join(conditions)

    df = pd.read_sql_query(query, conn, params=params)

    conn.close()

    return df

# Search by Product Model
def search_by_product(product):

    conn = sqlite3.connect(DB)

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

    conn = sqlite3.connect(DB)

    query = """
    SELECT 
        [Customer Name],
        [Phone Number],
        [Address],
        [Brand],
        [Model]
    FROM customers
    WHERE LOWER([Address]) LIKE LOWER(?)
    """

    df = pd.read_sql_query(query, conn, params=(f"%{location}%",))

    conn.close()

    return df