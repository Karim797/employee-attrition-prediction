import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EDA Dashboard", page_icon="📊", layout="wide")

st.markdown("""
<style>


.hero {
    background: linear-gradient(135deg, #0f172a, #1e3a8a);
    padding: 45px;
    border-radius: 22px;
    color: white;
    margin-bottom: 35px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
}

.hero p {
    font-size: 19px;
    color: #e5e7eb;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    padding: 12px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📊 Employee Attrition EDA Dashboard</h1>
    <p>
    Explore employee data, attrition distribution, department patterns,
    missing values, and HR-related trends.
    </p>
</div>
""", unsafe_allow_html=True)

col_nav1, col_nav2 = st.columns(2)

with col_nav1:
    if st.button("📊 EDA Dashboard"):
        st.switch_page("pages/1_EDA_Dashboard.py")

with col_nav2:
    if st.button("🤖 Prediction Page"):
        st.switch_page("pages/2_Employee_Attrition_Prediction.py")

st.markdown("---")

df = pd.read_csv("Employee_Attrition - Raw_DataSet.csv")

st.subheader("Dataset Overview")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("Rows", df.shape[0])

with c2:
    st.metric("Columns", df.shape[1])

with c3:
    if "Attrition" in df.columns:
        st.metric("Attrition Values", df["Attrition"].nunique())
    else:
        st.metric("Attrition Values", "N/A")

st.markdown("### Dataset Preview")
st.dataframe(df.head(10), use_container_width=True)

st.markdown("---")

if "Attrition" in df.columns:
    st.markdown("### Attrition Distribution")
    fig = px.histogram(
        df,
        x="Attrition",
        color="Attrition",
        title="Employee Attrition Count"
    )
    st.plotly_chart(fig, use_container_width=True)

if "Department" in df.columns:
    st.markdown("### Department Distribution")
    fig = px.histogram(
        df,
        x="Department",
        color="Department",
        title="Employees by Department"
    )
    st.plotly_chart(fig, use_container_width=True)

if "Gender" in df.columns and "Attrition" in df.columns:
    st.markdown("### Gender vs Attrition")
    fig = px.histogram(
        df,
        x="Gender",
        color="Attrition",
        barmode="group",
        title="Attrition by Gender"
    )
    st.plotly_chart(fig, use_container_width=True)

if "Monthly_Income" in df.columns:
    st.markdown("### Monthly Income Distribution")
    fig = px.histogram(
        df,
        x="Monthly_Income",
        nbins=40,
        title="Monthly Income Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("### Missing Values")
missing_df = df.isnull().sum().reset_index()
missing_df.columns = ["Column", "Missing Values"]
st.dataframe(missing_df, use_container_width=True)
