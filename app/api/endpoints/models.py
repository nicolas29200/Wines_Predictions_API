from fastapi import APIRouter

router = APIRouter()

@router.get("/model/")
async def home_model():
    return {"message" : "Je suis le router du model"} 