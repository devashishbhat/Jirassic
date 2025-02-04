from pydantic import BaseModel

class transcriptRequestBody(BaseModel):
    content: str

