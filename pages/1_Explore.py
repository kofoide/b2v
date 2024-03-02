import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
import os
 
# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="pygwalker",
    layout="wide"
)
 
# Add Title
st.title("Explore Your Data with Pygwalker In Streamlit")
 
def file_selector(folder_path='./data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)

# Import your data
df = pd.read_csv(filename)
 
# Generate the HTML using Pygwalker
pyg_html = pyg.to_html(df)
 
# Embed the HTML into the Streamlit app
components.html(pyg_html, height=1000, scrolling=True)
