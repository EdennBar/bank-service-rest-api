from pydantic import BaseModel
from typing import Optional

class TransactionBase(BaseModel):
    amount: float
    type: str

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
