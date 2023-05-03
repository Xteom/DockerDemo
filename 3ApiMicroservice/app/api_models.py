from pydantic import BaseModel


class PredictionRequest(BaseModel):
    field1: str
    field2: int


class PredictionResponse(BaseModel):
    prediction: str
