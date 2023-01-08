from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
    return {"message": "This is a poll app"}