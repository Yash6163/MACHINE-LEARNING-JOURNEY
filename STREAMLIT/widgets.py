import streamlit as st
import pandas as pd
st.snow()
st.title('Streamlit Text Input')
name=st.text_input("ENTER NAME : ")

age=st.slider("SELECT YOUR AGE : ",0,100,25)

options=['python','rust','cpp','js']
choice=st.selectbox("CHOOSE YOUR FAV LANGUAGE : ",options)
st. write(f"YOU SELECTED {choice}")
if name:
    st.write(f'HELLO {name}')

uploaded_file=st.file_uploader("choose a csv file : ",type='csv')

if uploaded_file is not None :
    df=pd.read_csv(uploaded_file)
    st.write(df)
    st.line_chart(df[['platform','post_type']].set_index("platform"))
