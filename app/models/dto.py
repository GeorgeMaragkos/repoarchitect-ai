from pydantic import BaseModel
from typing import Dict, List


class ScanResultDto(BaseModel):
    project_path: str
    file_count: int
    folder_count: int
    detected_files: List[str]
    detected_folders: Dict[str, bool]