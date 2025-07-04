# Imagem base leve com Python
FROM python:3.10-slim

# Instala dependências do sistema necessárias para PaddleOCR e OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Cria diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Atualiza o pip e instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que o Uvicorn irá usar
EXPOSE 8000

# Comando para iniciar o servidor FastAPI com reload desabilitado (modo produção)
CMD ["uvicorn", "ocr_app.app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
