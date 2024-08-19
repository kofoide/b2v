import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

@st.cache_data
def load_data():
    df = pd.read_csv('./data/2024_Week01.csv')

    # perform some transformation on the data
    # remove commas from the numbers
    df.replace(',', '', regex=True, inplace=True)

    # make date from year
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    # convert the columns to numeric
    df['Average Player Salary ($)'] = pd.to_numeric(df['Average Player Salary ($)'])
    df['Minimum Player Salary ($)'] = pd.to_numeric(df['Minimum Player Salary ($)'])

    return df

df = load_data()

tab_charts, tab_data = st.tabs(["Charts", "Data"])
with tab_charts:
    st.title("Line Charts")
    #df2 = df[['Year', 'Average Player Salary ($)']].set_index('Year')
 
    #Create a line chart with Y axis as Average Player Salary from lowest to highest
    st.line_chart(df, x='Year', y=['Average Player Salary ($)', 'Minimum Player Salary ($)'])

with tab_data:
    st.title("Explore Data")

    pr = df.profile_report()
    st_profile_report(pr)
