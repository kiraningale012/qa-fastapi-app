from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from schema.schema import QARequest
from services.service import qa_service
from utility.utility import templates

qarouter = APIRouter()



@qarouter.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@qarouter.post("/qa")
def answer_question(request: QARequest):
    return qa_service(request)
    
