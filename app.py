import streamlit as st 
import pandas as pd 
import plotly_express as px 

car_data = pd.read_csv("vehicles_us.csv")



st.header('Graficos sobre los autos anunciados')

st.write('elige el tipo de grafico que deseas visualizar')

hist_checkbox = st.checkbox('Construir histograma') # crear un botón
        
if hist_checkbox: # al hacer clic en el botón
        
    fig = px.histogram(car_data, x="type", color='transmission', title='tipos de transmision') 
          # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

scatter_checkbox = st.checkbox('Construir grafico de dispersion') # crear un botón
        
if scatter_checkbox: # al hacer clic en el botón
           # crear un histograma
    fig = px.scatter(car_data, x="odometer",  y="price", title='Odometros')    
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

pie_checkbox = st.checkbox('Construir grafico de pay')

if pie_checkbox:
     
     fig = px.pie(car_data, values='model_year', names='paint_color', title='Color mas popular')

     st.plotly_chart(fig, use_container_width=True)

hot_checkbox = st.checkbox('Construir mapa de calor')

if hot_checkbox:
     
     fig = px.density_heatmap(car_data, x="date_posted", y="type", title='Tipos de autos mas anunciados')

     st.plotly_chart(fig, use_container_width=True)
