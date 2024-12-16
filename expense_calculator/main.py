from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from users import models, schemas
from core.db import engine, Base, get_db

# Initialize database
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user)
    return db_user

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/expenses/", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    return crud.create_expense(db, expense)

@app.get("/expenses/{user_id}", response_model=list[schemas.Expense])
def read_expenses(user_id: int, db: Session = Depends(get_db)):
    return crud.get_expenses(db, user_id)
