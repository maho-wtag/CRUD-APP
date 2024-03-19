from fastapi import FastAPI
from routes.index import Student

app = FastAPI()

app.include_router(Student)