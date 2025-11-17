from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

from .model import iris_model


class PredictRequest(BaseModel):
    features: List[float]


class PredictResponse(BaseModel):
    predicted_class: str


app = FastAPI(title="ML API CI/CD Demo")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    if len(request.features) != 4:
        raise HTTPException(status_code=400, detail="features must be a list of 4 values")

    predicted_class = iris_model.predict_class(request.features)
    return PredictResponse(predicted_class=predicted_class)
