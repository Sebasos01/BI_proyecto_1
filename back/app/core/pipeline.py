class Pipeline:
    def __init__(self):
        # Inicializar componentes del pipeline si es necesario (e.g., cargar modelo entrenado)
        pass

    def predict(self, data):
        # Implementar la lógica para hacer predicciones
        # Aquí usarás el modelo cargado y devolverás predicciones con probabilidades
        return [{"prediction": "category_1", "probability": 0.75} for _ in data]

    def retrain(self, data, target):
        # Implementar la lógica para reentrenar el modelo
        # Deberás devolver métricas como Precision, Recall, F1-score
        return {"precision": 0.8, "recall": 0.7, "f1_score": 0.75}
