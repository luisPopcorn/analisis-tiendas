import streamlit as st
import pandas as pd

from analysis import analisis_tiendas
from explanation import explicacion_automatica
from charts import grafico_tiendas

st.set_page_config(
    page_title="Análisis Semanal de Tiendas",
    layout="wide"
)

st.title("📊 Análisis Automático de Tiendas")

archivo = st.file_uploader(
    "Sube el archivo de órdenes (CSV o Excel)",
    type=["csv", "xlsx"]
)

meta = 1000

if archivo:
    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo)
    else:
        df = pd.read_excel(archivo)

    col1, col2, col3 = st.columns(3)

    with col1:
        anio = st.selectbox(
            "Año",
            sorted(df["AnioContable"].unique())
        )

    with col2:
        semana = st.selectbox(
            "Semana",
            sorted(df["SemanaContable"].unique())
        )

    with col3:
        estado = st.selectbox(
            "Estado",
            ["todos", "cumplen", "no_cumplen"]
        )

    resultado = analisis_tiendas(
        df,
        anio=anio,
        semana=semana,
        meta=meta,
        estado=estado
    )

    st.subheader("📋 Resultado")
    st.dataframe(resultado, use_container_width=True)

    st.subheader("🧠 Análisis automático")
    st.text(explicacion_automatica(resultado))

    st.subheader("📊 Visualización")
    fig = grafico_tiendas(resultado)
    if fig:
        st.pyplot(fig)
    else:
        st.success("Todas las tiendas cumplen la meta.")
