from fastapi import FastAPI
import mysql.connector




app = FastAPI()

@app.get("/")
def databaseConnection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678",
        database="Student"
    )
    
    cursor = connection.cursor()
    database = "Student"
    try:
        # Check if the database exists
        cursor.execute("USE {}".format(database))
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_BAD_DB_ERROR:
            # Database doesn't exist, so create it
            cursor.execute("CREATE DATABASE {}".format(database))
            return {
                    "Response: ": "'Database {} created successfully.'.format(database)"
                }
        else:
            # Something went wrong while checking the database
            return {
                "Response: ": "err"
            }
    else:
        # Database already exists
        return {
            "Response: ": "Database {} already exists.".format(database)
        }
    
    # Close cursor and connection
    cursor.close()
    connection.close()

