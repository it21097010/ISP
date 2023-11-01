from fastapi import FastAPI
from typing import Dict
from . import predict as prd

allowed_origins = ["*"]
allowed_methods = ["*"]
allowed_headers = ["*"]

app = FastAPI()


@app.post("/pred/")
def predict(input:str):
    return int(prd.predict(input))