from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from database import get_session
from models.user import User

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI + SQLModel + Alembic"}

@app.post("/user")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@app.delete("/user/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return {"message": "User deleted"}
    return {"message": "User not found"}
    
@app.get("/users")
def read_users(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    users = session.exec(select(User).offset(skip).limit(limit)).all()
    return users