import streamlit as st
import pandas as pd
st.title("veri")
uploaded_file = st.file_uploader(" dosyanızı giriniz")
if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.subheader("Veri Dosyanız: ")
  #st.write(df.head())
  df
  st.subheader("filter: ")
  columns= df.columns.tolist()
  selected_column= st.selectbox("kolon", columns)
  filter_value = st.text_input("veri girişi")
  if selected_column and filter_value:
    filtered_df = df[df[selected_column].astype(str) == filter_value]
    st.write(filtered_df)

st.subheader("gorsellestırme: ")
x_column = st.selectbox("x ekseni için", columns)
y_column = st.selectbox("y ekseni icin", columns)
button= st.button("gorsellestr")
if button:
  st.line_chart(df,x=x_column, y=y_column)
  
  
