from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Importar el módulo del pipeline (tu clase Modelo actualizada)
from app.core.modelo import Modelo

router = APIRouter()

# Instancia del modelo
modelo = Modelo()

# Clases de solicitud y respuesta
class PredictionRequest(BaseModel):
    data: List[str]

class RetrainRequest(BaseModel):
    data: List[str]
    target: List[int]

# Endpoint para hacer predicciones (Endpoint 1)
@router.post("/predict")
async def predict(request: PredictionRequest):
    try:
        resultados = modelo.predict(request.data)
        print(resultados)
        return resultados
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para reentrenar el modelo (Endpoint 2)
@router.post("/retrain")
async def retrain(request: RetrainRequest):
    try:
        metrics = modelo.retrain(request.data, request.target)
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
