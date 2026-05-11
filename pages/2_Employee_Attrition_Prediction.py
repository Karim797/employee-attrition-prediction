import streamlit as st

st.set_page_config(page_title="Employee Attrition Predictor", page_icon="🤖", layout="wide")

st.markdown("""
<style>
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none;
}
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
.stButton button {
    width: 100%;
    background: linear-gradient(90deg, #0f172a, #2563eb);
    color: white;
    border-radius: 12px;
    padding: 14px;
    font-size: 18px;
    font-weight: 700;
    border: none;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>🤖 Employee Attrition Predictor AI</h1>
    <p>
    A smart HR analytics interface designed to estimate employee attrition risk
    using workplace, satisfaction, and performance indicators.
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

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👤 Employee Details")
    Age = st.number_input("Age", min_value=18, max_value=100, value=30)
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Marital_Status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
    Department = st.selectbox("Department", ["Sales", "HR", "Finance", "Marketing", "IT"])
    Job_Role = st.selectbox("Job Role", ["Assistant", "Manager", "Analyst", "Executive"])

with col2:
    st.markdown("### 🏢 Job Profile")
    Job_Level = st.slider("Job Level", 1, 5, 2)
    Monthly_Income = st.number_input("Monthly Income", min_value=0.0, value=10000.0)
    Years_at_Company = st.number_input("Years at Company", min_value=0.0, value=3.0)
    Work_Life_Balance = st.slider("Work Life Balance", 1, 4, 3)
    Overtime_input = st.selectbox("Overtime", ["No", "Yes"])

with col3:
    st.markdown("### 📈 Performance Metrics")
    Job_Satisfaction = st.slider("Job Satisfaction", 1, 5, 3)
    Work_Environment_Satisfaction = st.slider("Work Environment Satisfaction", 1, 4, 3)
    Relationship_with_Manager = st.slider("Relationship with Manager", 1, 4, 3)
    Absenteeism = st.number_input("Absenteeism Days", min_value=0.0, value=5.0)
    Average_Hours_Worked_Per_Week = st.number_input(
        "Average Hours Worked Per Week",
        min_value=0.0,
        value=40.0
    )

Overtime = 1 if Overtime_input == "Yes" else 0

st.markdown("---")

if st.button("🚀 Predict Attrition Risk"):

    risk_score = 0

    if Overtime == 1:
        risk_score += 1
    if Job_Satisfaction <= 2:
        risk_score += 1
    if Work_Environment_Satisfaction <= 2:
        risk_score += 1
    if Relationship_with_Manager <= 2:
        risk_score += 1
    if Absenteeism >= 7:
        risk_score += 1
    if Average_Hours_Worked_Per_Week >= 50:
        risk_score += 1
    if Work_Life_Balance <= 2:
        risk_score += 1

    st.markdown("## 🎯 Prediction Result")

    if risk_score <= 2:
        st.success("✅ Employee is likely to stay in the company.")
        st.info(f"Low Attrition Risk | Risk Score: {risk_score} / 7")

    elif risk_score <= 4:
        st.warning("⚠️ Employee has a moderate attrition risk.")
        st.info(f"Moderate Attrition Risk | Risk Score: {risk_score} / 7")

    else:
        st.error("🚨 Employee is likely to leave the company.")
        st.info(f"High Attrition Risk | Risk Score: {risk_score} / 7")
