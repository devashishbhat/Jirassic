from flask import jsonify
from flask_bcrypt import Bcrypt
from models.User import UserRegister, UserLogin
from models.Task import Task
from models.Transcript import transcriptRequestBody
from services.database import db
from services.task_generator import assign_tasks_from_transcript
from typing import List
import json

bcrypt = Bcrypt()

def hash_user_password(password:str) -> str:
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password

def verify_password(user_input_password:str, hashed_password:str) -> bool:
    return bcrypt.check_password_hash(user_input_password, hashed_password)

async def register_user_service(userObject: UserRegister):
    try:
        users_collection = db.user_details

        if not all(field in userObject for field in ['id', 'full_name', 'email', 'password', 'role']):
            return jsonify({"message": "Missing required fields"}), 400

        existing_user = users_collection.find_one({"email": userObject['email']})
        if existing_user:
            return jsonify({"message": "Email already registered"}), 400

        hashed_password = hash_user_password(userObject['password'])
        
        new_user = {
            "id": userObject['id'],
            "full_name": userObject['full_name'],
            "email": userObject['email'],
            "password_hash": hashed_password,
            "role": userObject['role'],
        }
        users_collection.insert_one(new_user)

        return jsonify({"message": "User registered successfully", "status": 200}), 200

    except Exception as e:
        return jsonify({"message": f"Error registering user: {str(e)}"}), 500

async def login_user_service(userObject: UserLogin):
    try:
        users_collection = db.user_details
        # Look for the user by email
        existing_user = users_collection.find_one({"email": userObject['email']})
        if existing_user:
            # Verify the provided password against the stored hashed password
            password_verification = verify_password(existing_user['password_hash'], userObject['password'])
            
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
        return jsonify({"message": f"Error logging in user: {str(e)}"}), 500

async def get_user_task(userId: int):
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
        return jsonify({"message": f"Error logging in user: {str(e)}"}), 500

async def generate_task_and_save(transcript: transcriptRequestBody):
    user_dictionary = await get_user_dictionary()

    # Get the task from LLM
    generate_task_by_llm = await assign_tasks_from_transcript(transcript)

    # Convert the task string to a JSON list
    parseable_task = convert_to_json(generate_task_by_llm)

    # Creating list of all the task according to Task schema
    final_task_list = process_tasks(parseable_task, user_dictionary)
    
    try:
        task_collection = db.task_details
        if final_task_list:
            task_dicts = [task.model_dump() for task in final_task_list]
            task_collection.insert_many(task_dicts)
            return {
                "message": "Task added, check database!",
                "status": 200
            }
        else:
            print("No tasks to insert.")
            return {
                "message": "No task to add in the database!",
                "status": 400
            }
    except Exception as e:
        return jsonify({"message": f"Error logging in user: {str(e)}"}), 500

def convert_to_json(data_str: str):
    try:
        modified_string = data_str.replace("json", "")
        data_json = json.loads(modified_string)
        return data_json
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"

async def get_user_dictionary():
    user_collection = db.user_details
    user_mapping = {}
    users = user_collection.find({}, {"full_name": 1, "id": 1})

    for user in users:
        user_mapping[user["full_name"]] = user["id"]  # full_name -> user_id

    return user_mapping

def process_tasks(ai_generated_tasks: List[dict], user_dictionary: dict) -> List[Task]:
    processed_tasks = []
    task_counter = 1  # Unique task ID counter

    for task in ai_generated_tasks:
        print(task)
        user_name = task["team_member_name"]
        user_id = user_dictionary.get(user_name)  # Get user_id from dictionary

        if user_id:  # Only add if user exists in the dictionary
            processed_tasks.append(Task(
                task_id=task_counter,
                user_id=user_id,
                user_name=user_name,
                task_desc=task["task_assigned"],
                story_points=task["story points"]
            ))
            task_counter += 1  # Increment task ID

    return processed_tasks



