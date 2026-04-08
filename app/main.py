from fastapi import FastAPI
from app.api.routes.upload import router as upload_router

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="RepoArchitect AI")

app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "RepoArchitect AI is running"}