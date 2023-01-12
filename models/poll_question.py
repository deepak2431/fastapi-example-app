from typing import Optional
from sqlmodel import Field, SQLModel, Session, select

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
    
    #update the marks with given question id
    def update_marks(question_id, marks):
        with Session(engine) as session:

            try: 
                statement = select(PollQuestion).where(PollQuestion.id==question_id)
                results = session.exec(statement)
                question = results.one()
                question.marks = marks
                session.add(question)
                session.commit()
                return 1
            except Exception as e:
                return 0
