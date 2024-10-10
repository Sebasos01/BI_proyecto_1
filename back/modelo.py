import joblib
import pandas as pd
import logging
from sklearn.metrics import precision_score, recall_score, f1_score
from datetime import datetime
import logging
import traceback
import importlib.util
import sys
import os


# Cargar los transformadores personalizados antes de cargar el modelo
base_dir = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.join(base_dir, "TransformadoresPersonalizados.py")

spec = importlib.util.spec_from_file_location("TransformadoresPersonalizados", module_path)
module = importlib.util.module_from_spec(spec)
sys.modules["TransformadoresPersonalizados"] = module
spec.loader.exec_module(module)


import os
import joblib
import pandas as pd
import logging
from sklearn.metrics import precision_score, recall_score, f1_score
from datetime import datetime
import traceback
import importlib.util
import sys

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

    def predecir(self, x_predecir):
        "X_predecir : dataframe"
        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = os.path.join(self.base_dir, 'logs', 'metadatos', f'prediccion_datos_{fecha_actual}.csv')

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

        x_predecir.to_csv(nombre_archivo, index=False)
        self.logger.info(f'Iniciando predicción. Cantidad de filas: {len(x_predecir)}, Columnas: {list(x_predecir.columns)}. Archivo de entrada: {nombre_archivo}')
        
        predicciones = []
        try:
            y_pred = self.modelo.predict(x_predecir)
            y_pred_proba = self.modelo.predict_proba(x_predecir)
            for i in range(len(y_pred)):
                predicciones.append(Prediccion(y_pred[i], y_pred_proba[i]))

            self.logger.info(f'Predicción exitosa. Cantidad de predicciones: {len(predicciones)}, Archivo de entrada: {nombre_archivo}')
        
        except Exception as e:
            error_message = traceback.format_exc()
            self.logger.error(f'Error en la predicción. Archivo de entrada: {nombre_archivo}. Error: {error_message}')
            predicciones = None

        return predicciones

    def configurar_logger(self):
        fecha_actual = datetime.now().strftime("%Y-%m-%d")
        nombre_log = os.path.join(self.base_dir, "logs", "metadatos", f'log_predicciones_{fecha_actual}.txt')

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
    
    def entrenar(self, x_train, y_train, ruta_df_test=None):
        if ruta_df_test is None:
            ruta_df_test = os.path.join(self.base_dir, "assets", "TestODScat_345.csv")

        fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        nombre_archivo = os.path.join(self.base_dir, 'logs', 'metadatos', f'{fecha_actual}.csv')

        # Crear el directorio si no existe
        os.makedirs(os.path.dirname(nombre_archivo), exist_ok=True)

        df_completo = pd.concat([x_train, y_train], axis=1)
        df_completo.to_csv(nombre_archivo, index=False)

        self.logger.info(f'Iniciando entrenamiento. Cantidad de filas: {len(x_train)}, Columnas: {list(x_train.columns)}. Cantidad de etiquetas {len(y_train)} Archivo de entrada: {nombre_archivo}')
        evaluacion = None
        try:
            nuevo_modelo = self.modelo.fit(x_train, y_train)
            self.modelo = nuevo_modelo
            joblib.dump(self.modelo, self.ruta_modelo)

            df_test = pd.read_csv(ruta_df_test)
            x_test = df_test.drop(columns=["sdg"])
            y_test = df_test["sdg"]
            y_pred_test = self.modelo.predict(x_test)

            precision = precision_score(y_test, y_pred_test, average='weighted')
            recall = recall_score(y_test, y_pred_test, average='weighted')
            f1 = f1_score(y_test, y_pred_test, average='weighted')
            evaluacion = Evaluacion(precision, recall, f1)
        
        except Exception as e:
            error_message = traceback.format_exc()
            self.logger.error(f'Error en el entrenamiento. Archivo de entrada: {nombre_archivo}. Error: {error_message}')
     
        return evaluacion





class Prediccion:
    def __init__(self, clase, probabilidad):
        self.clase = clase
        self.probabilidades = probabilidad


class Evaluacion:
    def __init__(self, precision, recall, f1_score):
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score


pepe = Modelo()

base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(base_dir, "assets", "TestODScat_345.csv")

predicciones = pepe.predecir(pd.read_csv(ruta_archivo).drop(columns = ["sdg"]))

for prediccion in predicciones:
    print(prediccion.clase, prediccion.probabilidades)



