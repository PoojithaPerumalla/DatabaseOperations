import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "********",
    "port": 5432
}

department = input("Enter department to search: ")

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, name, email, age, department FROM students WHERE department = %s",
        (department,)
    )

    rows = cursor.fetchall()

    print(f"Students in {department}:")
    if rows:
        for row in rows:
            print(row)
    else:
        print("No students found.")

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
