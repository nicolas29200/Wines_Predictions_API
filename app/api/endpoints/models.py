from fastapi import APIRouter
from app.model import model

router = APIRouter()

@router.get("/api/model")
async def model_serialise():
    return {"message" : "Permet d’obtenir le modèle sérialisé"}

@router.get("/api/model/description")
async def model_description():
    description=model.description()
    return description

@router.put("/api/model")
async def model_donnee_en_plus():
    return {"message" : "Permet d’enrichir le modèle d’une entrée de donnée supplémentaire"}

@router.post("/api/model/retrain")
async def model_retrain():
    return {"message" : "Permet de réentrainer le modèle"}
