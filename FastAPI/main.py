from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, List
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import SessionLocal, engine
import models

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

class UserBase(BaseModel):
    username: str
    password: int

class UserModel(UserBase):
    id: int

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()

    try: 
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

models.Base.metadata.create_all(bind=engine)


@app.post("/users/", response_model=UserModel)
async def create_user(user: UserBase, db: db_dependency):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@app.get("/users/", response_model=List[UserModel])
async def get_user(db: db_dependency, skip: int = 0, limit: int = 100):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users