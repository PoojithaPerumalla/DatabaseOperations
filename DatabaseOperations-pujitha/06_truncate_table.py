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

    cursor.execute("TRUNCATE TABLE students RESTART IDENTITY")

    conn.commit()
    print("students table truncated successfully.")
    print("All records have been removed and the ID sequence was reset.")

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
