from fastapi import APIRouter

router = APIRouter()

@router.get("/api/predict")
async def vin_parfait():
    return {"message" : "Permet de générer une combinaison de données permettant de fournir le vin parfait"}

@router.post("/api/predict")
async def vin_prediction():
    return {"message" : "Réalise une prédiction en donnant en body les données nécessaires du vin"}

