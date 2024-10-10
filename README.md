# Guía para correr el proyecto

Este proyecto contiene un backend desarrollado en Python con FastAPI y un frontend desarrollado con Vue.js. A continuación, se detallan los pasos para poner en marcha el backend y el frontend, así como sus dependencias y requisitos.

## Requisitos

- **Python 3.12.6**
- **Node.js 22.9.0**
- **npm 10.8.3**

## Instrucciones para poner en marcha el backend

### 1. Crear y activar un entorno virtual

Se recomienda utilizar un entorno virtual para manejar las dependencias de Python.

```bash
cd back
python3.12 -m venv venv
source venv/bin/activate   # En Linux o macOS
.\venv\Scripts\activate   # En Windows
```

### 2. Instalar las dependencias

Todas las dependencias están especificadas en el archivo `requirements.txt`. Usa el siguiente comando para instalar las dependencias del proyecto.

```bash
pip install -r requirements.txt
```

### 3. Descargar y configurar NLTK

Es necesario ejecutar el script `setnltk.py` para descargar los recursos necesarios de NLTK.

```bash
python back/app/core/setnltk.py
```

### 4. Ejecutar el backend con Uvicorn

Usa `uvicorn` para poner en marcha el servidor del backend. El siguiente comando iniciará el servidor en el puerto `8000`.

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Instrucciones para poner en marcha el frontend

### 1. Instalar las dependencias

Primero, asegúrate de que el backend esté corriendo. Luego, navega a la carpeta del frontend:

```bash
cd front
```

Instala las dependencias del frontend especificadas en el archivo `package.json` usando npm.

```bash
npm install
```

### 2. Ejecutar el frontend

Usa el siguiente comando para iniciar el servidor de desarrollo de Vue.js:

```bash
npm run serve
```

El frontend debería estar accesible en:

```
http://localhost:8080
```

A partir de este punto, el frontend estará en funcionamiento y se comunicará con el backend en el puerto `8000`.