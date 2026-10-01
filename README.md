# Informe Final: Laboratorio de Minería de Datos

## 1. Introducción y Pasos Realizados (Metodología CRISP-DM)

Basado en la metodología CRISP-DM, nos enfocamos en las fases de Modelado, Evaluación y preparación para el Despliegue. Los pasos técnicos realizados en cada escenario fueron:

- **Carga y Preparación de Datos:** Lectura de los datasets (`dolar_data.csv`, `glucosa_data.csv`, `energia_data.csv`) y separación de variables independientes ($X$) y la variable dependiente ($y$).
- **División de Datos:** Separación en conjuntos de entrenamiento (80%) y prueba (20%) para asegurar una correcta evaluación técnica.
- **Modelado:** Ajuste de modelos de Regresión Lineal Múltiple utilizando la librería `scikit-learn`.
- **Evaluación:** Cálculo de métricas de error (MSE, RMSE) y bondad de ajuste ($R^2$), junto con la interpretación de los coeficientes obtenidos.
- **Despliegue (Exportación):** Uso de la librería `joblib` para persistir (guardar) los modelos entrenados en archivos `.joblib`, y el desarrollo de un código para una interfaz web interactiva con Streamlit.

---

## 2. Análisis de Resultados

### Ejercicio 1: Predicción del Precio del Dólar
- **Desempeño del modelo:** El modelo logró un $R^2$ de 0.9963 y un MSE de 2376.97. Esto indica un ajuste casi perfecto, logrando explicar el 99.6% de la variabilidad del precio del dólar.
- **Interpretación de Coeficientes:**
  - **Día (4.98):** Muestra una tendencia incremental; por cada día adicional, el precio aumenta aproximadamente 5 unidades.
  - **Inflación (-870.73):** Es la variable con mayor sensibilidad matemática; un aumento en la tasa de inflación diaria está correlacionado negativamente con el precio del dólar.
  - **Tasa de interés (-1.37):** Tiene un impacto negativo leve.

### Ejercicio 2: Predicción de Niveles de Glucosa
- **Desempeño del modelo:** El modelo obtuvo un $R^2$ de 0.6814 y un MSE de 233.69. Es un desempeño moderado/aceptable, típico en contextos médicos con alta variabilidad humana.
- **Interpretación de Coeficientes y Mayor Impacto:**
  - **Edad (1.23) e IMC (0.93):** Tienen un impacto positivo. A mayor edad y mayor Índice de Masa Corporal, los niveles de glucosa tienden a subir.
  - **Actividad Física (-2.09):** Esta es la variable con mayor impacto. Tiene un coeficiente negativo fuerte, indicando que el ejercicio constante es el factor principal en este dataset para disminuir el nivel de glucosa en la sangre.

### Ejercicio 3: Consumo de Energía Eléctrica
- **Desempeño del modelo:** El modelo mostró un $R^2$ de 0.8968 y un RMSE de 20.72. Esto refleja un modelo muy sólido y confiable para predecir el consumo.
- **Interpretación de Coeficientes y Mayor Impacto:**
  - **Temperatura (9.95):** Se identificó sistemáticamente como la variable con mayor impacto (el coeficiente más alto). Significa que por cada grado Celsius extra, el consumo se incrementa en casi 10 kWh (muy probablemente por sistemas de enfriamiento/aire acondicionado).
  - **Hora (5.02):** Contribuye al incremento del consumo a medida que avanza el día.
  - **Día de la semana (-3.03):** Indica que hacia el final de la semana (fines de semana), el consumo eléctrico tiende a disminuir ligeramente.

---

## 3. Conclusiones

- **Efectividad de la Regresión Múltiple:** La técnica de regresión lineal múltiple resultó ser sumamente útil para estos tres problemas, logrando en dos de ellos (Dólar y Energía) ajustes sobresalientes ($R^2 > 0.89$), lo que garantiza predicciones altamente confiables.
- **Importancia de la Interpretabilidad:** Extraer los coeficientes permitió no solo hacer una "caja negra" que predice, sino responder preguntas del negocio o dominio (p. ej., demostrar matemáticamente que hacer ejercicio baja la glucosa, o que el calor dispara el consumo energético).
- **Transición a Producción:** La exportación de los modelos (archivos `.joblib`) cierra con éxito el ciclo CRISP-DM, habilitando la fácil integración de los algoritmos de Machine Learning en herramientas de usuario final, como la aplicación desarrollada con Flask/Streamlit.
