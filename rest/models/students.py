from sqlalchemy import Table, column
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta

students = Table(
    'students', meta
    Column('id', Integer, pr)
)