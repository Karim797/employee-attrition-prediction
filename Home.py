import streamlit as st

st.set_page_config(
    page_title="Employee Attrition AI",
    page_icon="🤖",
    layout="wide"
)

st.title(" Employee Attrition Prediction System")

st.write("""
An AI-powered HR analytics platform designed to analyze employee behavior,
visualize workforce insights, and predict attrition risk.
""")

st.markdown("---")

st.header("📌 Project Objectives")

st.write("""
- Analyze employee attrition trends
- Perform exploratory data analysis
- Build machine learning models
- Predict employee turnover risk
- Support HR decision-making
""")

st.markdown("---")
st.markdown("---")

st.header("📊 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Dataset Rows", "8,361")

with col2:
    st.metric("Features", "27")

with col3:
    st.metric("Target Classes", "2")

st.write("""
The dataset contains employee-related information such as demographics,
job role, department, income, satisfaction levels, work-life balance,
performance indicators, and attrition status.

The cleaned dataset was used in the dashboard to ensure consistent categories
such as gender, department, and attrition labels.
""")
st.header("🛠 Technologies Used")

st.write("""
- Python
- Pandas
- Scikit-Learn
- Plotly
- Streamlit
- Machine Learning
""")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("📊 Open EDA Dashboard"):
        st.switch_page("pages/1_EDA_Dashboard.py")

with col2:
    if st.button("🤖 Open Prediction Page"):
        st.switch_page("pages/2_Employee_Attrition_Prediction.py")
