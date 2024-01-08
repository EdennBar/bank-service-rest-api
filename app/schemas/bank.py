from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.schemas.user import UserBase


class BankBase(BaseModel):
    name: str
    location: Optional[str]
    established_date: Optional[datetime]

# Bank Create Model
class BankCreate(BaseModel):
    name: str

# Bank Model
class Bank(BankBase):
    accounts: List[UserBase] = []

