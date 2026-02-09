from typing import Annotated
from fastapi import FastAPI,Depends, HTTPException,Query
from sqlmodel import Field,Session,SQLModel,create_engine,select
from datetime import datetime
from contextlib import asynccontextmanager

class Note(SQLModel,table=True):
    id: int | None= Field(default=None,primary_key=True)
    title: str
    description: str | None = None
    time : datetime = Field(default_factory=datetime.now)

database = "sqlite:///database.db"
engine = create_engine(database,connect_args={"check_same_thread":False})

def create_all_eng():
    SQLModel.metadata.create_all(engine)

def start_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()

SessionDep = Annotated[Session,Depends(start_session)]

@asynccontextmanager  #instead of on_event which makes the code run only one time
async def lifespan(app: FastAPI):
    create_all_eng()
    yield

app = FastAPI(lifespan=lifespan)

#expections
# endpoints for (get_all, get_by_id, update (the time changes when update), create ,delete )
# use HTTPExecption for common errors (e.g., status_code=404 if the id you get is not found)


# for more, use from fastapi.templating -> Jinja2Templates for frontend 






