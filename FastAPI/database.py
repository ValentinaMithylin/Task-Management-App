from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# connecting to db
URL_DATABSE = "mysql+pymsql://root:@localhost:3306/TaskManagement"

engine = create_engine(URL_DATABSE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()