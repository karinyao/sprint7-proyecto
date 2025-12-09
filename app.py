import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Proyecto Sprint 7: Análisis Exploratorio de Datos")
st.write("¡Bienvenido a mi aplicación de análisis de datos!")

# Aquí irá tu análisis de datos
st.header("Instrucciones:")
st.write("""
1. Sube tu archivo de datos (CSV o Excel)
2. Explora las estadísticas
3. Visualiza los datos con gráficos interactivos
""")

# Ejemplo básico
df = pd.DataFrame({
    'Meses': ['Ene', 'Feb', 'Mar', 'Abr', 'May'],
    'Ventas': [100, 200, 150, 300, 250]
})

fig = px.bar(df, x='Meses', y='Ventas', title='Ventas Mensuales')
st.plotly_chart(fig)
