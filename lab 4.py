
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bhumi12*"
)

cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS CollegeDB")
cursor.execute("USE CollegeDB")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50),
    email VARCHAR(100)
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(50),
    credits INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Enrollment (
    enrollment_id INT PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
)
""")

print("Database and tables created successfully!")

cursor.close()
con.close()

