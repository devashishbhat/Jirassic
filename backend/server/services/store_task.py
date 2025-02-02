from services.task_generator import assign_tasks_from_transcript
from services.user import get_user_dictionary
from pymongo import MongoClient
from fastapi import HTTPException, status, Depends
from models.transcript import transcriptRequestBody
from models.task import Task
from services.database import get_database
from typing import List
import json

async def generate_task_and_save(transcript: transcriptRequestBody, db: MongoClient = Depends(get_database)):
    user_dictionary = await get_user_dictionary()
    print("User Dictionary: ", user_dictionary)

    # Get the task from LLM
    generate_task_by_llm = await assign_tasks_from_transcript(transcript)
    
    # Convert the task string to a JSON list
    parseable_task = convert_to_json(generate_task_by_llm)
    # print("Generated Tasks: ", parseable_task)

    # Creating list of all the task according to Task schema
    final_task_list = process_tasks(parseable_task, user_dictionary)
    # for task in final_task_list:
    #     print(task)
    
    try:
        task_collection = db.task_details
        if final_task_list:
            task_dicts = [task.model_dump() for task in final_task_list]
            task_collection.insert_many(task_dicts)
            print("Tasks successfully inserted into MongoDB!")
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
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error while adding task to mongoDB: {str(e)}"
        )

def convert_to_json(data_str: str):
    # Parse the string into a Python object (list of dictionaries)
    try:
        modified_string = data_str.replace("json", "")
        data_json = json.loads(modified_string)
        return data_json
    except json.JSONDecodeError as e:
        return f"Error decoding JSON: {str(e)}"

def process_tasks(ai_generated_tasks: List[dict], user_dictionary: dict) -> List[Task]:
    processed_tasks = []
    task_counter = 1  # Unique task ID counter

    for task in ai_generated_tasks:
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
