from pydantic import BaseModel

class Student(BaseModel):
    id: int
    name: str
    email: str
    roll: str
    Class: str
