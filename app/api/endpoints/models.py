from fastapi import APIRouter
from app.model import model
from app.model import read_add_csv
import os 

router = APIRouter()

@router.get("/api/model")
async def model_serialise():
    """Retourne le modèle séralisé

        Returns:
            dictionnaire: envoie le texte disant que le modèle est dejà sérialisé
        
    """
    texte="Le model est déjà sérialisé"
    if not os.path.isfile("app/model/modelXGBoost.json"):
        model.save_model()
        texte="Le model a été sérialisé"
    return {"message" : texte}


@router.get("/api/model/description")
async def model_description():
    """Retourne des informations sur le modèle

        Returns:
            dictionnaire: un dictionnaire avec des paramètres du modèles et la matrice des erreurs
            
    """
    description=model.description()
    return description


@router.put("/api/model")
async def model_donnee_en_plus(Id:int,fixedAcidity : float, volatileAcidity : float, 
                         citricAcid : float, residualSugar : float, 
                         chlorides : float, freeSulfurDioxyde : float,
                         totalSulfurDioxyde : float, density : float,
                         pH : float, sulphates : float, 
                         alcohol : float, quality : int):
    """Ajoute un vin dans le modèle

    Args:
        Id (int)
        fixedAcidity (float)
        volatileAcidity (float)
        citricAcid (float)
        residualSugar (float)
        chlorides (float)
        freeSulfurDioxyde (float)
        totalSulfurDioxyde (float)
        density (float)
        pH (float)
        sulphates (float)
        alcohol (float)
        quality (int)

    Returns:
        dictionnaire: message qu'une donnée a été rajouté au csv
    """
    new_Wine={"fixed acidity":fixedAcidity,"volatile acidity":volatileAcidity,"citric acid":citricAcid,"residual sugar":residualSugar,"chlorides":chlorides,"free sulfur dioxide":freeSulfurDioxyde,"total sulfur dioxide":totalSulfurDioxyde,"density":density,"pH":pH,"sulphates":sulphates,"alcohol":alcohol,"quality":quality,"Id":Id}
    read_add_csv.add_data(new_Wine)
    return {"message" : "une ligne a été rajouté à notre csv"}

@router.post("/api/model/retrain")
async def model_retrain():
    """Réentraine le modèle

    Returns:
        dictionnaire: message que le modèle a été réentrainer
    """
    model.save_model()

    return {"message" : "Le modèle à été réentrainé"}
