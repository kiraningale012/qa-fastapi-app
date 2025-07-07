
from http.client import HTTPException
from schema.schema import QARequest
from utility.utility import tokenizer, model, templates



def qa_service(request: QARequest):
    prompt = f"Context: {request.context}\nQuestion: {request.question}\nAnswer:"
    try:
        inputs = tokenizer(prompt, return_tensors="pt", truncation=True)
        outputs = model.generate(**inputs, max_new_tokens=150)
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))