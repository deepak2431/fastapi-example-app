from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class UserProfile(BaseModel):
    name: str
    description: str
    price: float = Field(gt = 10, description = "The price must be greater than 10")
    tax: float | None = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"item_id": item_id}

@app.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: str, item_id: str):
    return {
        "user": user_id,
        "item": item_id
    }

@app.post("/users/create_user")
async def create_user(user: UserProfile = Body(embed=True)):
    return {"name": user.name}