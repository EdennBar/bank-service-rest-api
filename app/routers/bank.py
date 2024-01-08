from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from app.services import db_bank
from app.schemas.bank import BankCreate


router = APIRouter(
    prefix='/bank',
    tags=['bank']
)

@router.post('/')
def create_bank(request: BankCreate, user_id:int ,db: Session = Depends(get_db)):
    return db_bank.create_bank_account_for_user(db, request,user_id)

