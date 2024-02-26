import streamlit as st
import pandas as pd
import os
import glob

def load_latest_csv():
    latest_csv = max(glob.glob('data/*.csv'), key=os.path.getctime)
    df = pd.read_csv(latest_csv)
    return df

# Function to show the 'Updates' page
def show_updates_page():
    st.header('Updates')

    latest_df = load_latest_csv()

    # Load the second-to-latest CSV file
    second_latest_csv = sorted(glob.glob('data/*.csv'), key=os.path.getctime)[-2]
    second_latest_df = pd.read_csv(second_latest_csv)

    # Merge the two DataFrames based on 'name'
    merged_df = pd.merge(second_latest_df, latest_df, on='name', how='inner', suffixes=('_old', '_new'))

    # Identify removed products
    removed_products = second_latest_df[~second_latest_df['name'].isin(merged_df['name'])]

    # Display removed products in a table
    if not removed_products.empty:
        st.subheader('Removed Products:')
        st.table(removed_products[['name', 'category', 'format', 'price', 'unit']])
    else:
        st.write('No products were removed.')


# Load the latest CSV
df = load_latest_csv()

# Sidebar for category selection
selected_category = st.sidebar.selectbox('Select Category:', df['category'].unique())

# Filter the DataFrame based on the selected category
filtered_df = df[df['category'] == selected_category]

# Rename columns and format 'Precio'
filtered_df = filtered_df.rename(columns={'name': 'Producto', 'format': 'Formato', 'price': 'Precio', 'unit': 'Unidad'})
filtered_df['Precio'] = filtered_df['Precio'].apply(lambda x: f'{x:.2f}')

# Display the filtered DataFrame in a table
st.table(filtered_df[['Producto', 'Formato', 'Precio', 'Unidad']])

# Show 'Updates' page if the button is clicked
if st.sidebar.button('Updates'):
    show_updates_page()
