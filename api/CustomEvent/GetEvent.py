import sqlite3

def GetEvents():
    try:
        connection = sqlite3.connect("./db/database.db")
        cursor = connection.cursor()

        cursor.execute("Select * From Events")
        events = cursor.fetchall()
        connection.close()
        return events
    except Exception as e:
        print("Error with the db Operation,", e)
        return None