from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.zip_service import save_and_extract_zip
from app.services.scan_service import scan_project_structure
from app.services.llm_service_review import generate_ai_review

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_project(file: UploadFile = File(...)):
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Only .zip files are allowed")

    extracted_path = save_and_extract_zip(file)

    scan_result = scan_project_structure(extracted_path)

    ai_review = generate_ai_review(scan_result)

    return {
    "message": "Project uploaded and scanned successfully",
    "scan_result": scan_result,
    "ai_review": ai_review
    }