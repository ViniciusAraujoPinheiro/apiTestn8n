from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ResponseModel(BaseModel):
    response: str

@app.get("/", response_model=ResponseModel)
def read_root():
    return {"response": "TESTE da api se tá funionando"}
