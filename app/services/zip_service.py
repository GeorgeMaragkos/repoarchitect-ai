#zip extraction logic
import zipfile
import shutil
from pathlib import Path
from uuid import uuid4
from fastapi import UploadFile
from app.core.config import UPLOADS_DIR


def save_and_extract_zip(file: UploadFile) -> Path:
    project_id = str(uuid4())
    zip_path = UPLOADS_DIR / f"{project_id}.zip"
    extract_path = UPLOADS_DIR / project_id

    with open(zip_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_path)

    return extract_path