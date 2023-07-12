from sqlalchemy.orm import Session

from . import models, schemas


def get_user_by_email(db: Session, email: str):
    return db.query(models.Users).filter(models.Users.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.Users(username=user.username, password=fake_hashed_password, email= user.email, name=user.name, createdAt=user.createdAt, updatedAt=user.updatedAt)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_alert(db: Session, alert: schemas.AlertCreate):
    db_alert = models.Alert(user_id=alert.user_id, coin_id=alert.coin_id, price=alert.price, createdAt=alert.createdAt, updatedAt=alert.updatedAt)
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def get_users(db: Session, user_id: int):
    return db.query(models.Users).filter(models.Users.id == user_id).first()

def get_coin(db: Session, coin_id: int):
    return db.query(models.Coin).filter(models.Coin.id == coin_id).first()

def get_alert(db: Session, user_id: int):
    return db.query(models.Alert).filter(models.Alert.user_id == user_id).all()

def show_coin(coin_id: int, coin_prince: int, db:Session):
    db_coin = get_coin(db, coin_id=coin_id)
    if db_coin.current_price > coin_prince:
        return {"message" : "SELL "+ db_coin.name} 
    return {"message" : "DONT SELL "+ db_coin.name}
