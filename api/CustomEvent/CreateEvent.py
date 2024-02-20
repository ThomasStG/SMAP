import sqlite3

def CreateEvent(title, description, date, time, location):
    try:
        connection = sqlite3.connect("./db/database.db")
        cursor = connection.cursor()

        cursor.execute("INSERT INTO Events (title, description, date, time, location) VALUES (?, ?, ?, ?, ?)", (title, description, date, time, location))
        connection.commit()
        connection.close()
        return True
    except sqlite3.Error as e:
        print("Error with the DB operation:", e)
        return False
