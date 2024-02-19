import streamlit as st
import pandas as pd

df = pd.read_csv('data/mercadona_products_190224_.csv')

selected_category = st.sidebar.selectbox('Select Category:', df['category'].unique())

filtered_df = df[df['category'] == selected_category]
st.table(filtered_df[['name', 'format', 'price', 'unit']])
