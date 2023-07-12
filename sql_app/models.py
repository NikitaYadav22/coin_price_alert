from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime,date 

from .database import Base

class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)
    createdAt = Column(String, default = datetime)
    updatedAt = Column(String, default= datetime)

    alert = relationship("Alert", back_populates="user")

class Coin(Base):
    __tablename__ = "coin"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    current_price = Column(Integer)
    # createdAt = Column(String, default = datetime)
    # updatedAt = Column(String, default= datetime)

    alert = relationship("Alert", back_populates="coin")

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Integer)
    status = Column(String, default= True)
    createdAt = Column(String, default = datetime)
    updatedAt = Column(String, default= datetime)
    user_id = Column(Integer, ForeignKey("users.id"))
    coin_id = Column(Integer, ForeignKey("coin.id"))

    user = relationship("Users", back_populates="alert")
    coin = relationship("Coin", back_populates="alert")

    
