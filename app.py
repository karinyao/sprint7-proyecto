import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Proyecto Sprint 7: Análisis Exploratorio de Datos")
st.write("¡Bienvenido a mi aplicación de análisis de datos!")
st.header('Análisis de Anuncios de Venta de Coches')

car_data = pd.read_csv('vehicles_us.csv')

# Mostrar información básica
st.write('Explorando el dataset de anuncios de venta de coches')
st.write(f'Total de anuncios: {len(car_data)}')

# Crear casilla de verificación para el histograma
build_histogram = st.checkbox('Construir histograma del kilometraje')

if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del Kilometraje",
                       labels={'odometer': 'Kilometraje'})
    
    # Mostrar gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear casilla de verificación para el gráfico de dispersión
build_scatter = st.checkbox('Construir gráfico de dispersión: Kilometraje vs Precio')

if build_scatter:
    st.write('Creación de un gráfico de dispersión mostrando la relación entre kilometraje y precio')
    
    # Crear gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title="Relación entre Kilometraje y Precio",
                     labels={'odometer': 'Kilometraje', 'price': 'Precio ($)'})
    
    # Mostrar gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)