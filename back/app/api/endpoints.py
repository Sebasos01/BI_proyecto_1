from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

# Importar el módulo del pipeline (aunque no implementaremos su lógica aquí)
from app.core.pipeline import Pipeline

router = APIRouter()

# Instancia del pipeline
pipeline = Pipeline()

# Definir un esquema de entrada para las predicciones
class PredictionRequest(BaseModel):
    data: List[dict]  # Los datos deben ser proporcionados como una lista de diccionarios

# Definir un esquema de entrada para el reentrenamiento
class RetrainRequest(BaseModel):
    data: List[dict]  # Los datos de entrenamiento
    target: List[int]  # Las etiquetas o categorías

# Endpoint para hacer predicciones (Endpoint 1)
@router.post("/predict")
async def predict(request: PredictionRequest):
    try:
        predictions = pipeline.predict(request.data)
        return {"predictions": predictions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para reentrenar el modelo (Endpoint 2)
@router.post("/retrain")
async def retrain(request: RetrainRequest):
    try:
        metrics = pipeline.retrain(request.data, request.target)
        return {"metrics": metrics}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
