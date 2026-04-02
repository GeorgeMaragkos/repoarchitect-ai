from fastapi import FastAPI
from app.api.routes.upload import router as upload_router

app = FastAPI(title="RepoArchitect AI")

app.include_router(upload_router)


@app.get("/")
def root():
    return {"message": "RepoArchitect AI is running"}