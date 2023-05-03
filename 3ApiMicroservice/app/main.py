from fastapi import FastAPI
from app.api_models import PredictionRequest, PredictionResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}


@app.post("/predict")
def predict(request: PredictionRequest) -> PredictionResponse:
    return {"prediction": "1"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
