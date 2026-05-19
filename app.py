
import streamlit as st
import pandas as pd

st.title("Optimisateur de Transport Public IA")

df = pd.read_csv("transport_data.csv")

st.subheader("Données")
st.dataframe(df)

st.subheader("Analyse")
ligne = st.selectbox("Choisir une ligne", df["ligne"].unique())

subset = df[df["ligne"] == ligne]

st.write("Passagers moyens :", round(subset["passagers"].mean(),2))
st.write("Retard moyen :", round(subset["retard_minutes"].mean(),2), "minutes")

if subset["passagers"].mean() > 100:
    st.success("Suggestion IA : augmenter la fréquence des autobus.")
else:
    st.info("Suggestion IA : maintenir le service actuel.")
