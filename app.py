import streamlit as st
import joblib
import numpy as np

# Cargar los modelos (asegúrate de que los archivos .joblib estén en el mismo directorio)
modelo_dolar = joblib.load('modelo_dolar.joblib')
modelo_glucosa = joblib.load('modelo_glucosa.joblib')
modelo_energia = joblib.load('modelo_energia.joblib')

st.title('Laboratorio: Predicciones de Minería de Datos')

# Menú de selección
opcion = st.sidebar.selectbox('Selecciona el modelo a utilizar:', 
                              ('Precio del Dólar', 'Nivel de Glucosa', 'Consumo de Energía'))

if opcion == 'Precio del Dólar':
    st.header('Predicción del Precio del Dólar')
    dia = st.number_input('Día', min_value=1, value=1)
    inflacion = st.number_input('Inflación (ej. 0.02)', format="%.4f", value=0.02)
    tasa = st.number_input('Tasa de interés (ej. 5.5)', format="%.2f", value=5.5)
    
    if st.button('Predecir Dólar'):
        pred = modelo_dolar.predict(np.array([[dia, inflacion, tasa]]))
        st.success(f'El precio estimado del dólar es: ${pred[0]:.2f}')
        
elif opcion == 'Nivel de Glucosa':
    st.header('Predicción de Nivel de Glucosa')
    edad = st.number_input('Edad', min_value=1, value=30)
    imc = st.number_input('IMC', format="%.2f", value=25.0)
    actividad = st.number_input('Horas de Actividad Física semanales', min_value=0, value=3)
    
    if st.button('Predecir Glucosa'):
        pred = modelo_glucosa.predict(np.array([[edad, imc, actividad]]))
        st.success(f'El nivel estimado de glucosa es: {pred[0]:.2f} mg/dL')

elif opcion == 'Consumo de Energía':
    st.header('Predicción de Consumo de Energía')
    temp = st.number_input('Temperatura (°C)', format="%.2f", value=25.0)
    hora = st.slider('Hora del día', 1, 24, 12)
    dia_semana = st.slider('Día de la semana (1=Lunes, 7=Domingo)', 1, 7, 1)
    
    if st.button('Predecir Consumo'):
        pred = modelo_energia.predict(np.array([[temp, hora, dia_semana]]))
        st.success(f'El consumo estimado es: {pred[0]:.2f} kWh')