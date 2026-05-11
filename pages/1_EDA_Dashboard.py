import streamlit as st
import pandas as pd

st.title("EDA Dashboard")

df = pd.read_csv("Employee_Attrition - Raw_DataSet.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)
