from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from app.models.user_model import User, Transaction
from app.schemas.trans import TransactionCreate



def create_transaction(request: TransactionCreate, user_id: int, db: Session):
    
    user = db.query(Transaction).filter(User.id == user_id).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_transaction = Transaction(
        user_id=user.id,
        type=request.type,
        amount=request.amount
    )
    
    if request.type == "deposit":
        user.amount += request.amount
    elif request.type == "withdraw":
        user.amount -= request.amount
        if user.amount < 0:
            raise HTTPException(status_code=400, detail="Insufficient funds")
    
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    
    return new_transaction