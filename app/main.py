from fastapi import FastAPI
from api.endpoints import model, predictions

app = FastAPI(
    title="FastAPI_Project_ING3_ICC_IA",
    version="0.1"
)

# Model et Predictions routes
app.include_router(model.router)
app.include_router(predictions.router)

@app.get("/")
async def home():
    return {"message" : "Hello World"}

