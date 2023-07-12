from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import action, models, schemas
from .database import SessionLocal, engine
from fastapi import FastAPI
from fastapi import BackgroundTasks, FastAPI

from typing import Union

app = FastAPI()


# def write_notification(email: str, message=""):
#     with open("log.txt", mode="w") as email_file:
#         content = f"notification for {email}: {message}"
#         email_file.write(content)


# @app.post("/send-notification/{email}")
# async def send_notification(email: str, background_tasks: BackgroundTasks):
#     background_tasks.add_task(write_notification, email, message="some notification")
#     return {"message": "Notification sent in the background"}


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = action.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return action.create_user(db=db, user=user)

@app.post("/alerts/", response_model=schemas.Alert)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return action.create_alert(db=db, alert=alert)

# @app.get("/users/", response_model=list[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = action.get_users(db, skip=skip, limit=limit)
#     return users

@app.get("/alerts/{user_id}", response_model=list[schemas.Message])
def read_alert(user_id: int, db: Session = Depends(get_db)):
    db_alert = action.get_alert(db, user_id=user_id)
    db_coin = []
    for alerts in db_alert:
        db_coin.append(action.show_coin(alerts.coin_id, alerts.price, db))
    if db_alert is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_coin

@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = action.get_users(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

 

# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
