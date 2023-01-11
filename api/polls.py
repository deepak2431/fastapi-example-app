from fastapi import APIRouter

from api.schema import Questions

router = APIRouter()


@router.get("/")
async def index():
    return {"message": "This is a poll app"}

@router.post("/question/create")
async def save_question(question: Questions):
    return {'subject': question.subject_name}