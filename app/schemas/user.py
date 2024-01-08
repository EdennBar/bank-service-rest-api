from pydantic import BaseModel
from typing import List,Optional
from datetime import datetime
class UserBase(BaseModel):
     email : str
     create_time: Optional[datetime]
     first_name : str
     last_name : str
     user_type : str
    
class UserCreate(BaseModel):
     hashed_password : str

class Users(UserBase):
     users: List[UserBase]

