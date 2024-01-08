from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from app.services import db_trans
from app.schemas.trans import TransactionCreate


router = APIRouter(
    prefix='/transactions',
    tags=['transactions']
)

@router.post('/{transaction_type}')
def create_transaction(request : TransactionCreate, user_id:int,db:Session = Depends(get_db)):
    return db_trans.create_transaction(request, user_id,db)  
