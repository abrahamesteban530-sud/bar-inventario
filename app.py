import streamlit as st
import pandas as pd

st.set_page_config(page_title="Inventario del Bar", layout="wide")

st.title("🍸 Inventario del Bar")

# Cargar inventario
df = pd.read_csv("inventario.csv")

# Mostrar tabla
st.dataframe(df, use_container_width=True)

# Filtro por categoría
categoria = st.selectbox("Filtrar por categoría", ["Todas"] + list(df["categoria"].unique()))

if categoria != "Todas":
    df = df[df["categoria"] == categoria]

# Alerta de bajo inventario
st.subheader("⚠️ Productos bajos")
bajo = df[df["cantidad"] <= 1]
st.dataframe(bajo)
