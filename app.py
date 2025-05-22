import streamlit as st
import pandas as pd
import joblib

# Chargement du modèle
model = joblib.load("model.pkl")

st.title("🌿 Diagnostic de Plante")

# Formulaire utilisateur
long_plante = st.number_input("Longueur de la plante (mm)", 0)
long_feuille = st.number_input("Longueur des feuilles (cm)", 0)
nb_feuilles = st.number_input("Nombre de feuilles", 0)
diam_feuille = st.number_input("Diamètre des feuilles (mm)", 0)
epaisseur_tige = st.number_input("Épaisseur de la tige (mm)", 0)
stomates_sup = st.number_input("Stomates face supérieure", 0)
stomates_inf = st.number_input("Stomates face inférieure", 0)
temperature = st.number_input("Température (°C)", 0)
humidite = st.number_input("Humidité (%)", 0)
solhumide = st.number_input("Humidité du sol (%)", 0)
lux = st.number_input("Luminosité (lux)", 0)

if st.button("Diagnostiquer"):
    data = pd.DataFrame([{
        'LongeurPlante': long_plante,
        'LongueurFeuille': long_feuille,
        'NombreFeuilles': nb_feuilles,
        'DiamètreFeuille': diam_feuille,
        'EpaisseurTige': epaisseur_tige,
        'StomatesSup': stomates_sup,
        'Stomatesinf': stomates_inf,
        'Temperature': temperature,
        'Humidite': humidite,
        'Solhumide': solhumide,
        'lux': lux
    }])

    prediction = model.predict(data)[0]

    if prediction == "Surveuillée":
        st.success("🌿 Plante en bonne santé")
    elif prediction == "Temoin":
        st.error("⚠️ Plante en mauvais état")
    else:
        st.warning("❓ État inconnu")
