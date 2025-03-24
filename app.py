from fastapi import FastAPI
from pydantic import BaseModel
from functions.consulta import *

app = FastAPI()

class ResponseModel(BaseModel):
    response: str

@app.get("/", response_model=ResponseModel)
def read_root():
    return {"response": "TESTE da api se tá funionando"}


@app.get("/seguros",response_model=ResponseModel)
def seguros():
    consulta()