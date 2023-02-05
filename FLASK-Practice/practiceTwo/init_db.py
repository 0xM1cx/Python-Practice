import sqlite3  



def openDatabase():
    connection = sqlite3.connect('instructors.db')
    cursor = connection.cursor()

    result = cursor.execute('''
        SELECT * FROM instructors;
    ''')

    print(cursor.fetchone())



    connection.close()



openDatabase()