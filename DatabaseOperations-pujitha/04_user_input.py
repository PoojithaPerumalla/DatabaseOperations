import psycopg2

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "********",
    "port": 5432
}

name = input("Enter student name: ")
email = input("Enter student email: ")
age = int(input("Enter student age: "))
department = input("Enter department: ")

try:
    conn = psycopg2.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Parameterized query prevents SQL injection.
    query = """
        INSERT INTO students (name, email, age, department)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, age, department))

    conn.commit()
    print("Student inserted successfully using a parameterized query.")

except psycopg2.Error as e:
    print("Database error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn" in locals():
        conn.close()
    print("Connection closed.")
