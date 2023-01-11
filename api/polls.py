from fastapi import APIRouter

from api.schema import Questions
from models.poll_question import PollQuestion

#init the router
router = APIRouter()

@router.get("/")
async def index():
    return {"message": "This is a question poll app"}

@router.post("/question/create")
async def save_question(question: Questions):
    
    question_details = PollQuestion(subject_name=question.subject_name,
                                    question_description=question.question_description,
                                    question=question.question,
                                    marks=question.marks)
    question_details.save()

    return {'message': 'Question processed successfully'}