
import streamlit as st
import random
import json

# Cargar las preguntas desde el archivo JSON
with open('dataset_preguntas.json', 'r') as f:
    datos = json.load(f)

st.title("🎓 Generador de Preguntas de Ciencias")

st.write("Selecciona un tema para obtener una pregunta aleatoria:")

tema = st.selectbox("Elige un tema:", ["biología", "física", "química"])

if st.button("Generar pregunta"):
    preguntas_tema = [p for p in datos['preguntas'] if p['tema'] == tema]
    if preguntas_tema:
        pregunta = random.choice(preguntas_tema)
        st.write(f"**Pregunta:** {pregunta['pregunta']}")
        mostrar = st.checkbox("Mostrar respuesta")
        if mostrar:
            st.write(f"✅ **Respuesta:** {pregunta['respuesta']}")
    else:
        st.write("No hay preguntas disponibles para este tema.")
