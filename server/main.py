from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import get_session
from models.user import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + SQLModel + Alembic"}

@app.get("/test")
def read_root():
    return {"message": "FastAPI + SQLModel + Alembic"}

@app.get("/users")
def read_users(session: Session = Depends(get_session)):
    return session.exec(select(User)).all()
