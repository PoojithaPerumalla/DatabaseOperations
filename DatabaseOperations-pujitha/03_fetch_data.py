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

    cursor.execute("SELECT id, name, email, age, department FROM students ORDER BY id")
    rows = cursor.fetchall()

    print("Student records:")
    for row in rows:
        print(row)

    cursor.execute("SELECT id, name, email, age, department FROM students ORDER BY id LIMIT 1")
    first_record = cursor.fetchone()
    print("\nFirst record using fetchone():")
    print(first_record)

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
