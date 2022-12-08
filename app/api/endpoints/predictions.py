from fastapi import APIRouter
import pandas as pd
router = APIRouter()
from app.model import model

@router.get("/api/predict")
async def vin_parfait():
    array_parameters=model.BestWinesParameters()
    return {"Those are the best parameters in order to have a perfect wine" : {"fixed acidity":array_parameters[0],"volatile acidity":array_parameters[1],"citric acid":array_parameters[2],"residual sugar":array_parameters[3],"chlorides":array_parameters[4],"free sulfur dioxide":array_parameters[5],"total sulfur dioxide":array_parameters[6],"density":array_parameters[7],"pH":array_parameters[8],"sulphates":array_parameters[9],"alcohol":array_parameters[10]}}

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

