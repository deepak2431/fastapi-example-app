from fastapi import FastAPI

from api.polls import router
from models.database import create_tables


#init the app   
app = FastAPI()

#register the routes
app.include_router(router, prefix="/polls")

#register the events
@app.on_event("startup")
def on_startup():
    create_tables()


