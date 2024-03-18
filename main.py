from fastapi import FastAPI
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="Student"
)

print(mydb)


app = FastAPI()

@app.get("/")
def read_something():
    return {"msg" : "Hello World"}

