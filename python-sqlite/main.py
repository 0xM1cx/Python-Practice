import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()



students = [("Shawn Michael A. Sudaria", "EVSU", 18), ("Chelsea P. Zarzuela", "EVSU", 18)]

cursor.executemany("insert into students values (?,?,?)", students)

for i in cursor.execute("select Name from students"):
    print(i)





connection.close()