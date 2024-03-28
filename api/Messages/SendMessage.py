import sqlite3


def Send(content):
    if len(content) <= 250:
        try:
            connection = sqlite3.connect("./db/database.db")
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO Messages (content) VALUES(?)", (content,))
            connection.commit()
            connection.close()
        except Exception as e:
            print("Error with the db Operation,", e)
            return None
    else:
        print("longer")


def Delete(id):
    try:
        connection = sqlite3.connect("./db/database.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM Messages WHERE id=?", (id,))
        connection.commit()
        connection.close()
    except Exception as e:
        print("Error with the db Operation:", e)
        return None


def Get():
    try:
        connection = sqlite3.connect("./db/database.db")
        cursor = connection.cursor()

        cursor.execute("Select * From Messages")
        events = cursor.fetchall()
        connection.close()
        return events
    except Exception as e:
        print("Error with the db Operation,", e)
        return None
