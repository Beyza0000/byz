import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    df = pd.read_csv(url, index_col=0)
    return df

url = 'https://raw.githubusercontent.com/Beyza0000/byz/refs/heads/main/penguins_examples.csv'
df = load_data()

st.write(df)

st.header("Result")
st.write(res)
