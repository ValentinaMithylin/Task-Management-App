from sqlalchemy import Column, String, Integer
from database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(Integer(4))


class Task(Base):
    __tablename__ = 'tasks'

    task_id = Column(Integer, primary_key=True, index=True)
    task_details = Column(String(100))
    task_status = Column(String(50))