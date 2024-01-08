from sqlalchemy.orm.session import Session

from app.schemas.bank import BankCreate
from app.models.user_model import User,Bank


def create_bank_account_for_user(db: Session, request: BankCreate, user_id:int):
    if request.name != 'BAC' and request.name != 'JPMORGAN' and request.name != 'Citigroup':
        raise Exception('The name of the bank is not supported')

    
    
    new_bank = Bank(name=request.name)
    db.add(new_bank)
    db.commit()
    db.refresh(new_bank)

    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.bank_id = new_bank.id
        db.commit()

    return new_bank