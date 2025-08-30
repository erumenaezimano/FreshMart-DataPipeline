import psycopg2
import pandas as pd

try:
    # Connect to freshmart db
    conn = psycopg2.connect(
        host="localhost",
        database="freshmart_db",
        user="postgres",
        password="Daimen100%", 
        port="5432"
    )
    print("Connected to FreshMart database")

    # Query 1: selects all diary products
    dairy = "SELECT * FROM products WHERE Category = 'Dairy';"
    df_dairy = pd.read_sql(dairy, conn)
    print("\n Products in Dairy category:")
    print(df_dairy)

    # Query 2: products with less than 50 Stock
    stock = "SELECT * FROM products WHERE StockQuantity < 50;"
    df_stock = pd.read_sql(stock, conn)
    print("\n Products with StockQuantity < 50:")
    print(df_stock)

    conn.close()

except Exception as e:
    print("Error:", e)