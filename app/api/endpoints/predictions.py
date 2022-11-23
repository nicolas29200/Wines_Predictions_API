from fastapi import APIRouter

router = APIRouter()

@router.get("/predictions/")
async def home_model():
    return {"message" : "Je suis le router des predictions"} 