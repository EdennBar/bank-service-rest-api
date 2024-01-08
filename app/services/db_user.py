
from fastapi import HTTPException,status
from app.schemas.user import UserBase
from sqlalchemy.orm.session import Session
from app.models.user_model import User
from ..services.user_services.user_factory import UserFactory

def create_user(db: Session, request: UserBase):
    user_type = UserFactory.create_user_type(request.user_type)
    if not user_type:
        raise ValueError("Failed to create user type")
    new_user = User(
        
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        user_type=request.user_type,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user():
    pass