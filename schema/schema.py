

from pydantic import BaseModel

class QARequest(BaseModel):
    context: str
    question: str