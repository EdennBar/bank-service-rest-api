
from fastapi import APIRouter,Depends
from app.schemas.user import UserBase
from sqlalchemy.orm import Session
from app.services import db_user
from core.database import get_db

router = APIRouter(
    prefix='/user',
    tags = ['user']
    )

@router.post('/')
def create(request: UserBase, db:Session = Depends(get_db)):
    return db_user.create_user(db, request)
