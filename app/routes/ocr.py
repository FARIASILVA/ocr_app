from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.ocr_service import process_image
import time

router = APIRouter()

@router.post("/")
async def detect_text(file: UploadFile = File(...)):
    start = time.time()

    try:
        result = await process_image(file)
        result["tempo_execucao_segundos"] = round(time.time() - start, 2)
        return result
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
