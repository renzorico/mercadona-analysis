# updates_page.py
import streamlit as st
import pandas as pd
import os
import glob

def load_latest_csv():
    latest_csv = max(glob.glob('data/*.csv'), key=os.path.getctime)
    return pd.read_csv(latest_csv)

# def show_updates_page():
#     st.header('Price Updates')

#     latest_df = load_latest_csv()

#     # Load the second-to-latest CSV file
#     second_latest_csv = sorted(glob.glob('data/*.csv'), key=os.path.getctime)[-2]
#     second_latest_df = pd.read_csv(second_latest_csv)

#     # Merge the two DataFrames based on 'name'
#     merged_df = pd.merge(second_latest_df, latest_df, on='name', how='outer', suffixes=('_old', '_new'))

#     # Identify added, removed, and changed products
#     added_products = merged_df[merged_df['price_old'].isna()]['name']
#     removed_products = merged_df[merged_df['price_new'].isna()]['name']
#     changed_products = merged_df[(merged_df['price_old'] != merged_df['price_new']) & ~merged_df['price_old'].isna() & ~merged_df['price_new'].isna()]

#     # Display updates
#     st.subheader('Added Products:')
#     for product in added_products:
#         st.write(f'{product} ---> Added')

#     st.subheader('Removed Products:')
#     for product in removed_products:
#         st.write(f'{product} ---> Removed')

#     st.subheader('Changed Prices:')
#     for index, row in changed_products.iterrows():
#         st.write(f'{row["name"]} ---> Old Price: {row["price_old"]} euros, New Price: {row["price_new"]} euros')
