<template>
  <div id="app" class="container">
    <h1>🌟 Modelo de Clasificación de Textos</h1>
    
    <!-- Sección para predicciones -->
    <section class="prediction-section">
      <h2>🔍 Predicción de Textos</h2>
      <textarea v-model="predictionInput" placeholder="Ingrese textos separados por líneas"></textarea>
      <br>
      <button @click="submitPrediction" class="primary-button">Obtener Predicciones</button>
      <div v-if="predictionResults.length > 0" class="results">
        <h3>Resultados:</h3>
        <ul>
          <li v-for="(result, index) in predictionResults" :key="index" class="prediction-item">
            <p><strong>Texto:</strong> {{ result.texto }}</p>
            <p><strong>Predicción:</strong> {{ getClassDesc(result.prediccion) }}</p>
            <p><strong>Probabilidades:</strong></p>
            <ul>
              <li v-for="(prob, clase) in result.probabilidades" :key="clase" :class="getClass(clase)">
                {{ getClassDesc(clase) }}: {{ (prob*100).toFixed(2) + "%" }}
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </section>
    
    <hr class="divider">
    
    <!-- Sección para reentrenamiento -->
    <section class="retrain-section">
      <h2>⚙️ Reentrenamiento del Modelo</h2>
      <input type="file" @change="handleFileUpload" accept=".csv" class="file-input">
      <br>
      <button @click="submitRetrain" :disabled="!retrainDataAvailable" class="primary-button">
        Reentrenar Modelo
      </button>
      <div v-if="loading" class="loading-spinner">🔄 Reentrenando modelo...</div>
      <div v-if="retrainMetrics" class="metrics">
        <h3>📊 Métricas de Reentrenamiento:</h3>
        <p><strong>Precisión:</strong> {{ retrainMetrics.precision }}</p>
        <p><strong>Recall:</strong> {{ retrainMetrics.recall }}</p>
        <p><strong>F1-Score:</strong> {{ retrainMetrics.f1_score }}</p>
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios';
import Papa from 'papaparse';

export default {
  name: 'App',
  data() {
    return {
      predictionInput: '',
      predictionResults: [],
      retrainDataAvailable: false,
      retrainData: [],
      retrainTarget: [],
      retrainMetrics: null,
      loading: false,
    };
  },
  methods: {
    submitPrediction() {
      const texts = this.predictionInput.split('\n').filter(text => text.trim() !== '');
      if (texts.length === 0) {
        alert('Por favor ingrese al menos un texto.');
        return;
      }
      axios.post('/api/predict', {
        data: texts
      })
      .then(response => {
        this.predictionResults = response.data;
      })
      .catch(error => {
        console.error(error);
        alert('Error al obtener las predicciones.');
      });
    },
    handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        Papa.parse(file, {
          header: true,
          complete: (results) => {
            const data = [];
            const target = [];
            if (!results.meta.fields.includes('Textos_espanol') || !results.meta.fields.includes('sdg')) {
              alert('El CSV debe contener las columnas "Textos_espanol" y "sdg".');
              return;
            }
            results.data.forEach(row => {
              if (row['Textos_espanol'] && row['sdg']) {
                data.push(row['Textos_espanol']);
                target.push(parseInt(row['sdg']));
              }
            });
            this.retrainData = data;
            this.retrainTarget = target;
            this.retrainDataAvailable = data.length > 0;
          },
          error: (error) => {
            console.error(error);
            alert('Error al leer el archivo CSV.');
          }
        });
      }
    },
    submitRetrain() {
      if (!this.retrainDataAvailable) {
        alert('No hay datos para reentrenar.');
        return;
      }
      this.loading = true;
      axios.post('/api/retrain', {
        data: this.retrainData,
        target: this.retrainTarget
      })
      .then(response => {
        this.retrainMetrics = response.data;
        this.loading = false;
        alert('Modelo reentrenado exitosamente.');
      })
      .catch(error => {
        console.error(error);
        alert('Error al reentrenar el modelo.');
        this.loading = false;
      });
    },
    getClass(clase) {
      if (clase === 5) return 'ods5';
      if (clase === 4) return 'ods4';
      if (clase === 3) return 'ods3';
      return '';
    },
    getClassDesc(clase) {
      if (clase === '5') return 'ODS 5 Igualdad de Género';
      if (clase === '4') return 'ODS 4 Educación de Calidad';
      if (clase === '3') return 'ODS 3 Salud y bienestar';
      return '';
    }
  }
}
</script>

<style>
body {
  background-color: #f7f7f7;
}

#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  margin: 20px auto;
  max-width: 800px;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  text-align: center;
  color: #34495e;
  font-size: 2rem;
  margin-bottom: 30px;
}

textarea {
  width: 100%;
  padding: 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  margin-bottom: 10px;
}

button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #3498db;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 1rem;
}

button:disabled {
  background-color: #ccc;
}

.primary-button {
  background-color: #27ae60;
}

hr.divider {
  margin: 40px 0;
  border: 0;
  height: 1px;
  background: #eee;
}

.prediction-section {
  margin-bottom: 30px;
}

.results {
  background-color: #f0f0f0;
  padding: 20px;
  border-radius: 6px;
}

ul {
  list-style: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

.prediction-item {
  padding: 10px;
  border-radius: 6px;
  background-color: #fafafa;
  border-left: 5px solid #3498db;
}

.ods5 {
  color: #d35400;
  font-weight: bold;
}

.ods4 {
  color: #8e44ad;
  font-weight: bold;
}

.ods3 {
  color: #27ae60;
  font-weight: bold;
}

.loading-spinner {
  font-size: 1.2rem;
  color: #3498db;
  margin-top: 10px;
}

.metrics {
  background-color: #ecf0f1;
  padding: 20px;
  border-radius: 6px;
}
</style>
