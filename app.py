from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import engine,SessionLocal
import models
import schemas


models.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/register")
def create_user(user:schemas.UserCreate,db:Session = Depends(get_db)):
    new_user = models.User(email=user.email,password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@app.get("/")
def home():
    return{"message" : "forex Trading Backend Running"}