import os
from dotenv import load_dotenv
from sqlmodel import SQLModel, create_engine

load_dotenv()

connection_url = os.getenv('CONNECTION_URL')

#create the engine
engine = create_engine(connection_url, echo=True)

def create_tables():

    from models.poll_question import PollQuestion
    SQLModel.metadata.create_all(engine)