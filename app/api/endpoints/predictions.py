from fastapi import APIRouter
import pandas as pd
router = APIRouter()
from app.model import model

@router.get("/api/predict")
async def vin_parfait():
    return {"message" : "Permet de générer une combinaison de données permettant de fournir le vin parfait"}

@router.post("/api/predict")
async def vin_prediction(fixedAcidity : float, volatileAcidity : float, 
                         citricAcid : float, residualSugar : float, 
                         chlorides : float, freeSulfurDioxyde : float,
                         totalSulfurDioxyde : float, density : float,
                         pH : float, sulphates : float, 
                         alcohol : float):
    wine={"fixed acidity":[fixedAcidity],"volatile acidity":[volatileAcidity],"citric acid":[citricAcid],"residual sugar":[residualSugar],"chlorides":[chlorides],"free sulfur dioxide":[freeSulfurDioxyde],"total sulfur dioxide":[totalSulfurDioxyde],"density":[density],"pH":[pH],"sulphates":[sulphates],"alcohol":[alcohol]}
    dico=pd.DataFrame(wine,index=[0])
    a=model.prediction(dico)
    return {"Le modèle a prédit que ce vin à cette note" : round(a[0])}

