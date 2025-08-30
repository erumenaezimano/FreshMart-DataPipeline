import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

try:
    #load cleaned dataset
    df = pd.read_csv("products.csv")

    #connect to freshmart_db
    conn = psycopg2.connect(
        host="localhost",
        database="freshmart_db",
        user="postgres",
        password="Daimen100%", 
        port="5432"
    )
    cur = conn.cursor()
    print("Connected to freshmart_db")

    #insert query
    insert_query = """
        INSERT INTO products (ProductName, Category, Price, StockQuantity)
        VALUES %s
    """

    #Convert DataFrame to list of tuples
    data = list(df[["ProductName", "Category", "Price", "StockQuantity"]].itertuples(index=False, name=None))

    #Bulk insert using execute_values
    execute_values(cur, insert_query, data)

    conn.commit()
    print("data inserted successfully!")

    #Close connection
    cur.close()
    conn.close()

except Exception as e:
    print("Error:", e)