### Paso a paso de la entrega de la Etapa 2 del proyecto de analítica de textos:

#### 1. **Automatización del modelo y desarrollo del API (Ingeniero de Datos)**
   - **Objetivo**: Crear un pipeline que automatice la preparación de datos, construcción, persistencia y acceso al modelo analítico mediante una API.
   - **Pasos**:
     1. Desarrollar un pipeline que incluya:
        - Preparación de datos.
        - Entrenamiento del modelo.
        - Persistencia del modelo en un repositorio.
     2. Implementar dos endpoints en la API REST:
        - **Endpoint 1**: Recibe datos en JSON para hacer predicciones con el modelo entrenado y devolver los resultados junto con las probabilidades.
        - **Endpoint 2**: Permite el re-entrenamiento del modelo con nuevos datos, devolviendo métricas de desempeño (Precision, Recall, F1-score). Proveer tres propuestas para re-entrenamiento y justificar cuál se implementa.
     3. Implementar logs para registrar entradas al modelo, datos de entrenamiento y resultados, para facilitar el análisis en caso de fallos.
   - **Entregable**: Documento describiendo el proceso automatizado, acompañado del código, y acceso a la API mediante endpoints definidos.

#### 2. **Desarrollo de la aplicación web o móvil (Ingeniero de Software)**
   - **Objetivo**: Construir una aplicación para que el usuario final pueda interactuar con el modelo y ver las predicciones con sus probabilidades.
   - **Pasos**:
     1. Diseñar la interfaz de usuario para facilitar la entrada de datos.
     2. Integrar la API desarrollada en la automatización con la aplicación.
     3. Permitir al usuario ingresar textos para obtener predicciones y probabilidades asociadas.
     4. Justificar el rol del usuario que utilizará la aplicación, su relación con el proceso de negocio y el valor que aporta.
   - **Entregable**: Aplicación funcional y justificación de su diseño, el rol de usuario y su valor.

#### 3. **Resultados y Video de la aplicación**
   - **Objetivo**: Mostrar cómo la aplicación es utilizada por el usuario final y destacar dos acciones que el usuario puede realizar basado en los resultados del modelo. En el video deben explicar su proyecto, incluyendo las decisiones tomadas sobre la preparación, los modelos implementados, las conclusiones del proceso, y la presentación y explicación de los resultados.
   - **Pasos**:
     1. Grabar un video (máximo 5 minutos) mostrando el uso de la aplicación y los resultados obtenidos.
     2. Explicar cómo el usuario puede tomar decisiones a partir de las predicciones.
     3. Relacionar el impacto de la aplicación con el contexto de Colombia y lo presentado en la entrega 1.
   - **Entregable**: Video publicado en el padlet, mostrando la simulación de la interacción y las decisiones del usuario.

#### 4. **Trabajo en equipo**
   - **Objetivo**: Documentar el proceso de trabajo en equipo, roles, tareas y reflexionar sobre la distribución de puntos.
   - **Pasos**:
     1. Asignar roles (líder de proyecto, ingeniero de datos, ingenieros de software).
     2. Describir las tareas asignadas a cada integrante, las horas dedicadas y los retos enfrentados.
     3. Reflexionar sobre el reparto de puntos entre los integrantes.
   - **Entregable**: Descripción de roles y tareas, reflexiones sobre el trabajo en equipo y distribución de puntos.

#### 5. **Otros entregables**
   - **Conjunto de datos**: Entregar los datos utilizados en la preparación del modelo.
   - **Repositorio en GitHub**: Subir el código al GitHub del grupo para que sea revisado.
   - **Condiciones de entrega**: El proyecto se realiza en grupos de 3 estudiantes, con documento de máximo 10 páginas (sin contar portada, tabla de contenido o referencias) y el video publicado en el padlet.
