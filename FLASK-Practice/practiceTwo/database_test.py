import sqlite3

conn = sqlite3.connect('instructors.db')
cur = conn.cursor()

data = []

result = cur.execute("SELECT * FROM instructors")
res = cur.fetchone()
# for i in result:
#     data.append(i)

def displayName(result):
    for b in result:
        next = input()
        if next != None:
            print(b[0], end="")

displayName(result)

conn.close()
# b = 0
# while b != len(data):
#     print(data[b][1], end="")
#     next = input()
#     if next != None:
#         b += 1