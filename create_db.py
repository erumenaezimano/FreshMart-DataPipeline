
import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Daimen100%",
    port="5432"
)
conn.autocommit = True  # allow database creation
cur = conn.cursor()

# Create freshmart_db
cur.execute("CREATE DATABASE freshmart_db;")

cur.close()
conn.close()