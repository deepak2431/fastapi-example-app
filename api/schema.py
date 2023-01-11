from pydantic import BaseModel

class Questions(BaseModel):
    subject_name: str
    question_description: str
    question: str
    marks: int