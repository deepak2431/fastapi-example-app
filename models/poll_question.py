from typing import Optional
from sqlmodel import Field, SQLModel, Session

from .database import engine

class PollQuestion(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subject_name: str
    question_description: str
    question: str
    marks: int

    def __init__(self,
                    subject_name,
                    question_description,
                    question,
                    marks):
        
        self.subject_name = subject_name
        self.question_description = question_description
        self.question = question
        self.marks = marks
    
    def save(self):
        with Session(engine) as session:
            session.add(self)
            session.commit()
