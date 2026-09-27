# Database Operations using Python

This project demonstrates basic PostgreSQL database operations using Python and psycopg2.

## Requirements
- PostgreSQL
- Python 3
- psycopg2-binary

Install the Python library:
    pip install psycopg2-binary

## Before running
Edit DB_CONFIG in each Python file if your PostgreSQL username/password/database are different.

Default local settings:
- host: localhost
- port: 5432
- user: postgres
- database: postgres

## Files
1. 01_create_table.py - Connects to PostgreSQL and creates the students table.
2. 02_insert_data.py - Inserts sample records.
3. 03_fetch_data.py - Fetches and displays records using fetchone/fetchall.
4. 04_user_input.py - Takes user input and inserts it using a parameterized query.
5. 05_where_condition.py - Uses SELECT with a WHERE condition.
6. 06_truncate_table.py - Demonstrates TRUNCATE TABLE.
7. psql_commands.sql - PostgreSQL/psql commands for database and table operations.

## Important
Run the scripts only after PostgreSQL is running. Take screenshots of the VS Code code and the actual terminal output after running each task, and place them in the screenshots folder.
