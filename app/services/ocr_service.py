from fastapi import UploadFile, HTTPException
from paddleocr import PaddleOCR
from PIL import Image, UnidentifiedImageError
from io import BytesIO
import numpy as np
import cv2

from app.utils.image_utils import desenhar_resultados, encode_image_base64

ocr = PaddleOCR(use_angle_cls=True, lang='en')

async def process_image(file: UploadFile):
    contents = await file.read()

    try:
        image = Image.open(BytesIO(contents)).convert("RGB")
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="Arquivo enviado não é uma imagem válida.")

    image_np = np.array(image)
    image_cv = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

    result = ocr.ocr(image_cv)

    textos_filtrados = []
    for linha in result:
        for elemento in linha:
            if not isinstance(elemento, list) or len(elemento) != 2:
                continue
            box, (text, conf) = elemento
            textos_filtrados.append({
                "text": text,
                "confidence": float(conf),
                "box": box
            })

    image_annotada = desenhar_resultados(image_cv.copy(), textos_filtrados)
    imagem_base64 = encode_image_base64(image_annotada)

    return {
        "textos_detectados": textos_filtrados,
        "imagem_annotada_base64": imagem_base64
    }
