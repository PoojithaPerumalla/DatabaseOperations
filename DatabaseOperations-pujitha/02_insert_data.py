import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "********",
    "port": 5432
}

records = [
    ("Poojitha", "poojitha@example.com", 21, "CSE"),
    ("Anjali", "anjali@example.com", 22, "ECE"),
    ("Rahul", "rahul@example.com", 21, "IT")
]

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.executemany("""
        INSERT INTO students (name, email, age, department)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (email) DO NOTHING
    """, records)

    conn.commit()
    print("Records inserted successfully.")

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
