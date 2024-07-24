from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import logging

# Configurar el logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar el modelo
try:
    model = joblib.load('models\modelo_random_forest.pkl')
    scaler = joblib.load('models/scaler.pkl')
    logger.info("Modelo cargado correctamente.")
except Exception as e:
    logger.error(f"Error al cargar el modelo: {e}")
    raise HTTPException(status_code=500, detail="Error al cargar el modelo")

app = FastAPI()


class PredictionRequest(BaseModel):
    # Define las características que tu modelo necesita para hacer una predicción
    nota_parcial_media: float
    nota_parcial_mediana: float
    score_media: float
    score_mediana: float
    frecuencia_tareas: float
    frecuencia_examenes: float
    tiempo_entrega: float


@app.post("/predict/")
def predict(data: PredictionRequest):
    try:
        # Convierte los datos de entrada a un formato adecuado para el modelo
        input_data = np.array([[
            data.nota_parcial_media,
            data.nota_parcial_mediana,
            data.score_media,
            data.score_mediana,
            data.frecuencia_tareas,
            data.frecuencia_examenes,
            data.tiempo_entrega
        ]])

        # Escalar los datos de entrada
        input_scaled = scaler.transform(input_data)
        # Realiza la predicción
        prediction = model.predict(input_scaled)

        # Redondear la predicción a un decimal
        rounded_prediction = round(prediction[0], 1)

        return {"prediction": rounded_prediction}
    except Exception as e:
        logger.error(f"Error al realizar la predicción: {e}")
        raise HTTPException(
            status_code=500, detail="Error al realizar la predicción")


@app.get("/")
def read_root():
    return {"message": "Welcome to the prediction API"}
