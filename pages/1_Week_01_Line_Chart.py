import pandas as pd
import streamlit as st
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling import st_profile_report

@st.cache_data
def load_data():
    df = pd.read_csv('./data/2024_Week01.csv')
    df.replace(',', '', regex=True, inplace=True)

    # make date from year
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    return df

df = load_data()

tab_charts, tab_data = st.tabs(["Charts", "Data"])
with tab_charts:
    st.title("Line Charts")
    #df2 = df[['Year', 'Average Player Salary ($)']].set_index('Year')
    st.line_chart(df, x='Year', y='Average Player Salary ($)')

with tab_data:
    st.title("Explore Data")
    pr = ProfileReport(df, explorative=True)
    st_profile_report(pr, navbar=True)
