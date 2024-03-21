from fastapi import FastAPI
import mysql
import mysql.connector 

app = FastAPI()
@app.get("/arafat")
def api_call():
    return {"hello", "world"}


connection = mysql.connector.connect(
        host="localhost",
        user="root",
        database="Student",
        password="12345678"
    )
    
cursor = connection.cursor()
database = "Student"

from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    email: str
    roll: str
    Class: str


@app.get("/")
def databaseConnection():
    
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
    
@app.get("/read")
def read_data():
    cursor = connection.cursor()
    query = "SELECT * FROM studentInfo"
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows

@app.get("/read/{ }")
def read_data(student_id: int):
    cursor = connection.cursor()
    query = "SELECT * FROM studentInfo WHERE id = %s"
    try:
        # Execute the query with the provided id
        cursor.execute(query, (student_id,))
        
        # Fetch the result
        result = cursor.fetchone()
        
        # Close the cursor
        cursor.close()
        
        if result:
            return result
        else:
            return {"msg": "Record not found"}
    except mysql.connector.Error as error:
        return {"msg": f"Error retrieving data: {error}"}



@app.post("/insert")
def create_data(student: Student):
    cursor = connection.cursor()
    # Define the SQL query for insertion with placeholders
    query = "INSERT INTO studentInfo (id, name, roll, email, Class) VALUES (%s, %s, %s, %s, %s)"
    # Define the values to be inserted
    student_values = (student.id, student.name, student.roll,  student.email, student.Class)
    #why cursor isnot execute
    try:
        # Execute the query with the provided values
        cursor.execute(query, student_values)
        
        # Commit the transaction
        connection.commit()
        
        # Close the cursor
        cursor.close()
        
        return {"msg": "Data inserted successfully"}
    except mysql.connector.Error as error:
        # Rollback the transaction in case of an error
        connection.rollback()
        cursor.close()
        return {"msg": f"Error inserting data: {error}"}
    
@app.put("/update/{id}")
def update_data(student: Student):
    cursor = connection.cursor()
    query = "UPDATE studentInfo SET name = %s, email = %s, roll = %s, Class = %s WHERE id = %s"
    # Define the values to be used in the query
    student_values = (student.name, student.email, student.roll, student.Class, student.id)
    # Execute the query with the provided values
    try:
        # Execute the query with the provided values
        cursor.execute(query, student_values)
        
        # Commit the transaction
        connection.commit()
        
        # Close the cursor
        cursor.close()
        
        return {"msg": "Data updated successfully"}
    except mysql.connector.Error as error:
        # Rollback the transaction in case of an error
        connection.rollback()
        cursor.close()
        return {"msg": f"Error updating data: {error}"}

@app.delete("/delete/{id}")
def delete_data(id: int):
    cursor = connection.cursor()
    query = "DELETE FROM studentInfo where id = %s"
    try:
        # Execute the query with the provided id
        cursor.execute(query, (id,))
        
        # Commit the transaction
        connection.commit()
        
        # Check if any rows were affected by the deletion
        if cursor.rowcount > 0:
            return {"message": "Data deleted successfully"}
        else:
            return  {"message": "Data cannot be deleted"}
        
    except mysql.connector.Error as error:
        return  {"message": "Data cannot be deleted"}    
        cursor.close()
