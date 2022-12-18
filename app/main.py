from fastapi import FastAPI
from app.api.endpoints import predictions
from app.api.endpoints import models

app = FastAPI(
    title="FastAPI_Project_ING3_ICC_IA",
    version="0.1"
)

# Model et Predictions routes
app.include_router(models.router)
app.include_router(predictions.router)

@app.get("/")
async def home():
    """Racine de l'API

    Returns:
        dicionnaire: message de bienvenu
    """
    return {"message" : "Bienvenue sur notre prédicteur de qualité de vin!"}

