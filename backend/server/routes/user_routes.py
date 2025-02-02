from fastapi import APIRouter, Depends, Query
from models.user import UserRegister, UserLogin
from models.transcript import transcriptRequestBody
from services.user import register_user_service, login_user_service, get_user_task
from services.database import get_database
from services.store_task import generate_task_and_save

user_router = APIRouter()

@user_router.post("/register")
async def register_user(user_data: UserRegister, db=Depends(get_database)):
    return await register_user_service(user_data, db)

@user_router.post("/login")
async def login_user(user_data:UserLogin, db=Depends(get_database)):
    return await login_user_service(user_data, db)

@user_router.post("/generate-task")
async def task_generator(generatedTranscript: transcriptRequestBody, db=Depends(get_database)):
    return await generate_task_and_save(generatedTranscript, db)

@user_router.get("/get-task")
async def get_task_db(userId: int = Query(..., description="The ID of the user"), db=Depends(get_database)):
    return await get_user_task(userId, db)
