from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.ocr import router as ocr_router

app = FastAPI(title="OCR API")

# CORS para testes locais
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra rotas
app.include_router(ocr_router, prefix="/detect")
