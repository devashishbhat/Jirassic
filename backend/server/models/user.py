from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: int
    full_name: str
    email: str
    password_hash: str
    role: str
    #expertise field which is an array
    created_at: datetime = datetime.utcnow()

    class Settings:
        collections = "user_details"

    def __repr__(self):
        return f"<User {self.full_name}>"

class UserRegister(BaseModel):
    id: int
    full_name: str
    email: str
    password: str
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: str
    password: str
