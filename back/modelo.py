import joblib
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score

class Modelo:
    def __init__(self, ruta_modelo = ".assets/pipeline_modelo.joblib"):
        self.ruta_modelo = ruta_modelo
        self.modelo = joblib.load(ruta_modelo)
    
    def predecir(self, x_predecir):
        "X_predecir : dataframe"
        y_pred = self.modelo.predict(x_predecir)
        y_pred_proba = self.modelo.predict_proba(x_predecir)
        predicciones = []

        
        for i in range(len(predicciones)):
            predicciones.append(Prediccion(y_pred[i], y_pred_proba[i]))

        return predicciones
    
    def entrenar(self, x_train, y_train, ruta_df_test = ".assets/TestODScat_345"):
        nuevo_modelo = self.modelo.fit(x_train, y_train)
        self.modelo = nuevo_modelo
        joblib.dump(self.modelo, self.ruta_modelo)
        
        df_test = pd.read_csv(ruta_df_test)

        x_test = df_test.drop(columns = ["sdg"])
        y_test = df_test["sdg"]

        y_pred_test = self.modelo.predict(x_test)

        precision = precision_score(y_test, y_pred_test, average='weighted')
        recall = recall_score(y_test, y_pred_test, average='weighted')
        f1 = f1_score(y_test, y_pred_test, average='weighted')

        

        return Evaluacion(precision,recall,f1)




class Prediccion:
    def __init__(self, clase, probabilidad):
        self.clase = clase
        self.probabilidades = probabilidad


class Evaluacion:
    def __init__(self, precision, recall, f1_score):
        self.precision = precision
        self.recall = recall
        self.f1_score = f1_score
