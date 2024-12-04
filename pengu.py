import streamlit as st
import pandas as pd
import streamlit_pandas as sp

@st.cache_data
def load_data():
    df = pd.read_csv(url, index_col=0)
    return df

url = 'https://raw.githubusercontent.com/Beyza0000/byz/refs/heads/main/penguins_examples.csv'
df = load_data()
create_data = {"studyName": "text",
                "Sample": "multiselect",
                "Number": "multiselect",
        }

all_widgets = sp.create_widgets(df, create_data, ignore_columns=["Individual ID"])
res = sp.filter_df(df, all_widgets)
st.title("Streamlit AutoPandas")
st.header(" DataFrame")
st.write(df)

st.header("Result")
st.write(res)
