from fastapi import APIRouter, Depends
from models.user import UserRegister
from services.user import register_user_service
from services.database import get_database

user_router = APIRouter()

@user_router.post("/register")
async def register_user(user_data: UserRegister, db=Depends(get_database)):
    return await register_user_service(user_data, db)
