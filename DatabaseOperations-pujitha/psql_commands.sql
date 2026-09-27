-- Run these commands in psql or pgAdmin Query Tool.

-- Create a database (run while connected to the postgres database):
CREATE DATABASE database_operations;

-- Connect to it in psql:
-- \c database_operations

-- Create table:
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    age INTEGER,
    department VARCHAR(50)
);

-- Insert records:
INSERT INTO students (name, email, age, department)
VALUES
('Poojitha', 'poojitha@example.com', 21, 'CSE'),
('Anjali', 'anjali@example.com', 22, 'ECE'),
('Rahul', 'rahul@example.com', 21, 'IT');

-- Fetch records:
SELECT * FROM students;

-- WHERE condition:
SELECT * FROM students WHERE department = 'CSE';

-- TRUNCATE:
TRUNCATE TABLE students RESTART IDENTITY;

-- Drop table if required:
-- DROP TABLE students;

-- Drop database if required:
-- DROP DATABASE database_operations;
