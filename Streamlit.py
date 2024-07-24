import streamlit as st
import requests

st.title("Predicción de Nota Final de Materia")

# Inputs del usuario
nota_parcial_media = st.number_input(
    "Nota Parcial Media", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
nota_parcial_mediana = st.number_input(
    "Nota Parcial Mediana", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
score_mediana = st.number_input(
    "Score Mediana", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
score_media = st.number_input(
    "Score Media", min_value=0.0, max_value=10.0, value=5.0, step=0.1)
tiempo_entrega = st.number_input(
    "Tiempo de Entrega", min_value=0.0, max_value=100.0, value=10.0, step=0.1)
frecuencia_tareas = st.number_input(
    "Frecuencia de Tareas", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
frecuencia_examenes = st.number_input(
    "Frecuencia de Exámenes", min_value=0.0, max_value=100.0, value=5.0, step=0.1)

# Botón de predicción
if st.button("Predecir Nota Final"):
    data = {
        "nota_parcial_media": nota_parcial_media,
        "nota_parcial_mediana": nota_parcial_mediana,
        "score_media": score_media,
        "score_mediana": score_mediana,
        "frecuencia_tareas": frecuencia_tareas,
        "frecuencia_examenes": frecuencia_examenes,
        "tiempo_entrega": tiempo_entrega
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict/", json=data
        )
        response.raise_for_status()  # Lanza un error para códigos de estado HTTP no 200
        prediction = response.json().get("prediction")
        st.write(f"La predicción de la nota final es: {prediction}")
    except requests.exceptions.RequestException as e:
        st.write(f"Error al realizar la predicción: {e}")
