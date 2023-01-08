from fastapi import FastAPI

from api.polls import router


#init the app   
app = FastAPI()

#register the routes
app.include_router(router, prefix="/polls")


