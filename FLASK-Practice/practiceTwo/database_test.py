import sqlite3

conn = sqlite3.connect('instructors.db')
cur = conn.cursor()

data = []

result = cur.execute("SELECT * FROM instructors")
for i in result:
    data.append(i)

conn.close()
b = 0
while b != len(data):
    print(data[b][1], end="")
    next = input()
    if next != None:
        b += 1