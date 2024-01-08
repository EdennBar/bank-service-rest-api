import datetime
from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from core.database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    user_type = Column(String)
    email = Column(String, unique=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    balance = Column(Float, default=0.0)  # Add balance column
    
    bank_id = Column(Integer, ForeignKey('bank.id'), unique=True)  # unique=True ensures one-to-one relationship
    bank = relationship("Bank", back_populates="user")
    transactions = relationship("Transaction", back_populates="user")
    
    

class Bank(Base):
    __tablename__ = 'bank'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String, nullable=True)
    established_date = Column(DateTime, default=datetime.datetime.utcnow)
    
    
    user = relationship("User", back_populates="bank")


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    type = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="transactions")
