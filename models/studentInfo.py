from sqlalchemy import Table, Column
from config.db import meta
from sqlalchemy.sql.sqltypes import Integer, String

student = Table(
    'studentInfo', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('roll', String(255)),
    Column('class', String(255))
)