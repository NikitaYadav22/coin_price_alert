from pydantic import BaseModel
from datetime import datetime,date

class CustomBase(BaseModel):
    createdAt: datetime
    updatedAt: datetime

class UserCreate(CustomBase):
    name: str
    email: str
    username: str
    password: str

class User(UserCreate, CustomBase):
    id: int
    is_active: bool
    
    class Config:
        orm_mode = True

class CoinCreate(BaseModel):
    name: str
    current_price = int

class Coin(CoinCreate):
    id: int

    class Config:
        orm_mode = True

    
class AlertCreate(CustomBase):
    price: int
    user_id: int
    coin_id: int

class Message():
    message: str
    
class Alert(AlertCreate, Message, CustomBase):
    id: int
    status: str
   
    class Config:
        orm_mode = True

