Aquí tienes el código actualizado para utilizar Anaconda en lugar de un entorno virtual de Python:

# BI_proyecto_1

Este repositorio contiene los archivos y notebooks utilizados en la primera entrega del proyecto de Business Intelligence.

## Documento de la Primera Entrega

[Acceder al documento en Overleaf](https://es.overleaf.com/read/wtgfyxnnrmyh#120450)

## Código del Notebook de la Primera Entrega

[Acceder al código en este repositorio](https://github.com/Sebasos01/BI_proyecto_1/blob/main/proyecto_1_entrega_1.ipynb)

## Video de la Primera Entrega

[Acceder al video en Youtube](youtube.com)

## Presentación de la Primera Entrega

[Acceder a la presentación en Canva](canva.com)

## Cómo Clonar y Ejecutar este Proyecto

Para clonar y ejecutar este proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el Repositorio

Primero, necesitas clonar este repositorio a tu máquina local. Abre tu terminal y ejecuta el siguiente comando:

```bash
git clone https://github.com/Sebasos01/BI_proyecto_1.git
```

### 2. Navegar al Directorio del Proyecto

Después de clonar el repositorio, navega al directorio del proyecto:

```bash
cd BI_proyecto_1
```

### 3. Crear un Entorno de Anaconda

Es recomendable crear un entorno de Anaconda para gestionar las dependencias de Python. Puedes crear un entorno ejecutando:

```bash
conda create --name mi_entorno python=3.11
```

> **Nota:** Cambia `mi_entorno` por el nombre que prefieras para tu entorno y ajusta `python=3.11` a la versión de Python que necesites.

### 4. Activar el Entorno de Anaconda

Activa el entorno de Anaconda:

```bash
conda activate mi_entorno
```

### 5. Instalar las Dependencias

Una vez que el entorno de Anaconda esté activo, instala las dependencias necesarias utilizando el archivo `requirements.txt`. Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

### 6. Ejecutar el Notebook

Con todas las dependencias instaladas, ahora puedes ejecutar el notebook de Jupyter. Inicia Jupyter Notebook con el siguiente comando:

```bash
jupyter notebook
```

Esto abrirá el Jupyter Notebook en tu navegador. Navega al archivo `.ipynb` que deseas ejecutar y comienza a trabajar.

## Uso de `pip freeze`

El comando `pip freeze` se utiliza para capturar todas las dependencias de Python que están instaladas en tu entorno de Anaconda. Esto es útil para crear un archivo `requirements.txt` que lista todas las bibliotecas y versiones necesarias para ejecutar el proyecto en otro entorno.

Para generar un archivo `requirements.txt`, ejecuta el siguiente comando:

```bash
pip freeze > requirements.txt
```

Este comando crea un archivo `requirements.txt` en el directorio actual que contiene todas las bibliotecas de Python instaladas en el entorno de Anaconda y sus versiones específicas. Este archivo puede ser compartido con otros para que puedan replicar el mismo entorno de desarrollo.

## Extensiones Recomendadas para Visual Studio Code

Para trabajar de manera más eficiente en este proyecto, recomendamos instalar las siguientes extensiones de Visual Studio Code:

1. **Python** - Proporciona soporte completo para Python, incluyendo IntelliSense, linting, depuración, y ejecución de scripts.
2. **Jupyter** - Permite ejecutar y editar notebooks de Jupyter directamente en Visual Studio Code.

Este código actualizado ahora utiliza Anaconda para gestionar el entorno Python, facilitando la administración de dependencias y versiones.