from fastapi import FastAPI
from database import engine
import routers,models


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

app.include_router(routers.router)

