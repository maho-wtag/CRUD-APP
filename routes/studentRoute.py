from fastapi import APIRouter
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from config.db import connection
from models.index import Student
from schemas.index import Student

student = APIRouter()

@student.get("/")
async def read_data():
    return connection.execute(Student.select()).fetchall()

@student.get("/{id}")
async def read_data(id: int):
    return connection.execute(Student.select().where(Student.c.id == id)).fetchall()

@student.post("/")
async def write_data(Student):
    return connection.execute(Student.insert().values(
        id = Student.id,
        name = Student.name,
        roll = Student.roll,
        email = Student.email,
        Class = Student.Class
    ))

@student.put("/{id}")
async def update_data(id: int, student: Student):
    connection.execute(student.update().values(
        id = student.id,
        name = student.name,
        roll = student.roll,
        email = student.email,
        Class = student.Class
    )).where(student.c.id == id)
    return connection.execute(student.select()).fetchall()

@student.delete("/{id}")
async def delete_data():
    connection.execute(student.delete).where(student.c.id == id)
    return connection.execute(student.select()).fetchall()