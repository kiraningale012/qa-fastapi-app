from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.router import qarouter

app = FastAPI(title="QA API")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(qarouter, tags=["Question Answering"])



