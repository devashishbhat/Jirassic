from pydantic import BaseModel

class Task(BaseModel):
    task_id: int
    user_id: int
    user_name: str
    task_desc: str
    story_points: int
