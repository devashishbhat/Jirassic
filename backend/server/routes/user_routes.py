from fastapi import APIRouter, Depends
from models.user import UserRegister, UserLogin
from services.user import register_user_service, login_user_service
from services.database import get_database

user_router = APIRouter()

@user_router.post("/register")
async def register_user(user_data: UserRegister, db=Depends(get_database)):
    return await register_user_service(user_data, db)

@user_router.post("/login")
async def login_user(user_data:UserLogin, db=Depends(get_database)):
    return await login_user_service(user_data, db)
