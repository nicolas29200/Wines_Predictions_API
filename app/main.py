from fastapi import FastAPI

app = FastAPI(
    title="FastAPI_Project_ING3_ICC_IA",
    version="0.1"
)

@app.get("/")
def home():
    return {"message" : "Hello World"}

