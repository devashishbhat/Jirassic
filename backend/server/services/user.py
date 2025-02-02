from models.user import User, UserRegister, UserLogin
from models.task import Task
from services.database import get_database
from fastapi import HTTPException, status, Depends
from pymongo import MongoClient
import bcrypt

def hash_user_password(password:str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(user_input_password:str, hashed_password:str) -> bool:
    return bcrypt.checkpw(user_input_password.encode('utf-8'), hashed_password.encode('utf-8'))

async def register_user_service(userObject: UserRegister, db: MongoClient = Depends(get_database)):
    hashed_password = hash_user_password(userObject.password)

    new_user = User(
        id=userObject.id,
        full_name=userObject.full_name,
        email=userObject.email,
        password_hash=hashed_password, 
        role=userObject.role,
    )

    # print(new_user.dict())    THIS IS PRINTING!

    try:
        users_collection = db.user_details
        existing_user = users_collection.find_one({"email": userObject.email})
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        new_user_1 = new_user.model_dump()
        users_collection.insert_one(new_user_1)

        return {
            "message": "User registered successfully",
            "status": 200
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error registering user: {str(e)}"
        )

async def login_user_service(userObject: UserLogin, db: MongoClient = Depends(get_database)):
    try:
        users_collection = db.user_details
        existing_user = users_collection.find_one({"email": userObject.email})
        if existing_user:
            password_verification = verify_password(userObject.password, existing_user["password_hash"])
            if password_verification:
                return {
                    "message": "Login successful",
                    "userData": {
                        "id": existing_user["id"],
                        "name": existing_user["full_name"],
                        "role": existing_user["role"],
                    },
                    "status": 200
                }
            
            return {
                "message": "Wrong Password",
                "status": 400
            }
        
        return {
            "message": "Please register yourself first",
            "status": 400
        }

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error loging user: {str(e)}"
        )

async def get_user_dictionary():
    db = await get_database()
    user_collection = db.user_details
    user_mapping = {}
    users = user_collection.find({}, {"full_name": 1, "id": 1})

    for user in users:
        user_mapping[user["full_name"]] = user["id"]  # full_name -> user_id

    return user_mapping

async def get_user_task(userId: int, db: MongoClient = Depends(get_database)):
    try:
        task_details = db.task_details
        if userId==1:
            tasks = task_details.find()
        else:
            tasks = task_details.find({"user_id": userId})
        task_list = [Task(**task) for task in tasks]
        if not task_list:
            return {
                "status":400,
                "message": "No task are assigned to you right now!"
            }
        
        return task_list
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching tasks: {str(e)}")
