import streamlit as st
import pandas as pd

df = pd.read_csv('data/mercadona_products_190224_.csv')

selected_category = st.sidebar.selectbox('Select Category:', df['category'].unique())

filtered_df = df[(df['category'] == selected_category)]

filtered_df = filtered_df.rename(columns={'name': 'Producto', 'format': 'Formato', 'price': 'Precio', 'unit': 'Unidad'})
filtered_df['Precio'] = filtered_df['Precio'].apply(lambda x: f'{x:.2f}')
st.table(filtered_df[['Producto', 'Formato', 'Precio', 'Unidad']])
