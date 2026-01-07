from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import Base, engine, get_db
from models import User

app = FastAPI()
Base.metadata.create_all(bind=engine)

class UserSchema(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "Hello FastAPI 🚀"}

@app.post("/users")
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
