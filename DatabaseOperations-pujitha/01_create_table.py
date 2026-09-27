import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "********",
    "port": 5432
}

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(150) UNIQUE NOT NULL,
            age INTEGER,
            department VARCHAR(50)
        )
    """)

    conn.commit()
    print("Connected to PostgreSQL successfully.")
    print("students table created successfully.")

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
