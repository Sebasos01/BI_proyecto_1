import os
import joblib
import pandas as pd
import logging
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from datetime import datetime
import traceback
import importlib.util
import sys
from typing import List, Dict

class Modelo:
    def __init__(self, ruta_modelo=None):
        # Cargar los transformadores personalizados
        self.cargar_transformadores_personalizados()
        
        # Usar siempre la ubicación de modelo.py para construir rutas relativas
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        if ruta_modelo is None:
            # Construir la ruta completa hacia el modelo basado en la ubicación de este archivo
            ruta_modelo = os.path.join(self.base_dir, "assets", "pipeline_modelo.joblib")
    
        self.ruta_modelo = ruta_modelo
        self.modelo = joblib.load(ruta_modelo)
        self.logger = self.configurar_logger()

    def cargar_transformadores_personalizados(self):
        """Carga los transformadores personalizados para asegurarse de que estén disponibles para el modelo."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        module_path = os.path.join(base_dir, "TransformadoresPersonalizados.py")

        spec = importlib.util.spec_from_file_location("TransformadoresPersonalizados", module_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules["TransformadoresPersonalizados"] = module
        spec.loader.exec_module(module)

    def predict(self, textos: List[str]) -> List[Dict[str, float]]:
        """
        Recibe una lista de textos y devuelve una lista de predicciones con sus probabilidades.
        """
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = os.path.join(self.base_dir, 'logsModelo', 'metadatos', f'prediccion_datos_{fecha_actual}.csv')

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

        # Crear un DataFrame a partir de los textos
        df_textos = pd.DataFrame({'Textos_espanol': textos})
        df_textos.to_csv(nombre_archivo, index=False)
        self.logger.info(f'Iniciando predicción. Cantidad de textos: {len(textos)}. Archivo de entrada: {nombre_archivo}')
        
        resultados = []
        try:
            # Realizar predicciones
            y_pred = self.modelo.predict(df_textos)
            y_pred_proba = self.modelo.predict_proba(df_textos)
            clases = self.modelo.classes_

            for idx in range(len(y_pred)):
                prediccion = {
                    'texto': textos[idx],
                    'prediccion': str(y_pred[idx].item()),
                    'probabilidades': dict(zip([str(c.item()) for c in clases], [str(x.item()) for x in y_pred_proba[idx]]))
                }
                resultados.append(prediccion)

            self.logger.info(f'Predicción exitosa. Cantidad de predicciones: {len(resultados)}. Archivo de entrada: {nombre_archivo}')
        
        except Exception as e:
            error_message = traceback.format_exc()
            self.logger.error(f'Error en la predicción. Archivo de entrada: {nombre_archivo}. Error: {error_message}')
            raise e  # Propagar la excepción para que FastAPI pueda manejarla

        return resultados

    def configurar_logger(self):
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        nombre_log = os.path.join(self.base_dir, "logsModelo", "metadatos", f'log_predicciones_{fecha_actual}.txt')

        # Crear un logger personalizado
        logger = logging.getLogger('modelo_logger')

        # Configurar solo si el logger no tiene handlers para evitar duplicados
        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)

            # Crear un handler para escribir en el archivo de log
            file_handler = logging.FileHandler(nombre_log)
            file_handler.setLevel(logging.INFO)

            # Crear un formato para los logs
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Agregar el handler al logger
            logger.addHandler(file_handler)

        return logger
    
    def retrain(self, textos: List[str], etiquetas: List[int]) -> Dict[str, float]:
        """
        Recibe listas de textos y etiquetas, reentrena el modelo y devuelve las métricas de evaluación.
        """
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = os.path.join(self.base_dir, 'logsModelo', 'datos', f'entrenamiento_datos_{fecha_actual}.csv')

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

        # Crear DataFrame de entrenamiento
        df = pd.DataFrame({'Textos_espanol': textos, 'sdg': etiquetas})
        df.to_csv(nombre_archivo, index=False)

        self.logger.info(f'Iniciando reentrenamiento. Cantidad de textos: {len(textos)}. Archivo de entrada: {nombre_archivo}')
        evaluacion = {}

        try:
            # Dividir los datos en conjuntos de entrenamiento y prueba
            X_train, X_test, y_train, y_test = train_test_split(
                df[['Textos_espanol']], df['sdg'], test_size=0.2, random_state=42
            )

            # Reentrenar el modelo
            nuevo_modelo = self.modelo.fit(X_train, y_train)
            self.modelo = nuevo_modelo
            joblib.dump(self.modelo, self.ruta_modelo)

            # Evaluar el modelo con el conjunto de prueba
            y_pred_test = self.modelo.predict(X_test)

            # Calcular las métricas de evaluación
            precision = precision_score(y_test, y_pred_test, average='weighted')
            recall = recall_score(y_test, y_pred_test, average='weighted')
            f1 = f1_score(y_test, y_pred_test, average='weighted')

            evaluacion = {
                'precision': precision,
                'recall': recall,
                'f1_score': f1
            }

            self.logger.info(f'Reentrenamiento exitoso. Métricas: {evaluacion}')

        except Exception as e:
            error_message = traceback.format_exc()
            self.logger.error(f'Error en el reentrenamiento. Archivo de entrada: {nombre_archivo}. Error: {error_message}')
            raise e  # Propagar la excepción para que FastAPI pueda manejarla

        return evaluacion
