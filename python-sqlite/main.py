from multiprocessing import connection
import sqlite3

connection = sqlite3.connect("students.db")
cursor = sqlite3.cursor()

cursor.execute("create table students (Name text, School text, Age integer)")

students = [("Shawn Michael A. Sudaria", "EVSU", 18), ("Chelsea P. Zarzuela", "EVSU", 18)]

cursor.execute(many)

connection.close()