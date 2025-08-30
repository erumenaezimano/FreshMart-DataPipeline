import psycopg2

try:
    # Connect to the freshmart DB
    conn = psycopg2.connect(
        host="localhost",
        database="freshmart_db",
        user="postgres",
        password="Daimen100%",
        port="5432"
    )
    cur = conn.cursor()

    # Create Products table
    create_table_query = """
    CREATE TABLE products (
        ProductID SERIAL PRIMARY KEY,
        ProductName VARCHAR(100),
        Category VARCHAR(50),
        Price DECIMAL(10,2),
        StockQuantity INT
    );
    """
    cur.execute(create_table_query)
    conn.commit()
    print("Products table created successfully!")

    cur.close()
    conn.close()

except Exception as e:
    print(" Error:", e)