from models.user import User, UserRegister
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
