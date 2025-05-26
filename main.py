# app.py
import pandas as pd
import plotly.express as px
import streamlit as st

# Google Drive 데이터 다운로드 URL
file_url = 'https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY'

@st.cache_data
def load_data():
    df = pd.read_csv(file_url)
    return df

df = load_data()

st.title("당뇨병 진단 데이터 시각화")
st.write("데이터 미리 보기:")
st.dataframe(df.head())

# 예: Glucose vs BMI 산점도
fig = px.scatter(df, x="Glucose", y="BMI", color="Outcome",
                 title="혈당(Glucose) vs BMI (당뇨 여부에 따른 색 구분)",
                 labels={"Outcome": "당뇨 여부 (1=Yes, 0=No)"})

st.plotly_chart(fig)
