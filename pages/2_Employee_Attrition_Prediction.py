import streamlit as st

# Page Title
st.title("Employee Attrition Prediction")

st.write(
    "Enter employee information below to estimate the likelihood "
    "of employee attrition."
)

st.markdown("---")

# Employee Information
st.header("Employee Information")

Age = st.number_input(
    "Age",
    min_value=18,
    max_value=100,
    value=30
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Marital_Status = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

Department = st.selectbox(
    "Department",
    ["Sales", "HR", "Finance", "Marketing", "IT"]
)

Job_Role = st.selectbox(
    "Job Role",
    ["Assistant", "Manager", "Analyst", "Executive"]
)

Job_Level = st.slider(
    "Job Level (1 = Entry Level, 5 = Senior Level)",
    1,
    5,
    2
)

Monthly_Income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=10000.0
)

Years_at_Company = st.number_input(
    "Years at Company",
    min_value=0.0,
    value=3.0
)

Work_Life_Balance = st.slider(
    "Work Life Balance (1 = Poor, 4 = Excellent)",
    1,
    4,
    3
)

Job_Satisfaction = st.slider(
    "Job Satisfaction (1 = Low, 5 = High)",
    1,
    5,
    3
)

Work_Environment_Satisfaction = st.slider(
    "Work Environment Satisfaction (1 = Poor, 4 = Excellent)",
    1,
    4,
    3
)

Relationship_with_Manager = st.slider(
    "Relationship with Manager (1 = Poor, 4 = Excellent)",
    1,
    4,
    3
)

Absenteeism = st.number_input(
    "Absenteeism Days",
    min_value=0.0,
    value=5.0
)

Average_Hours_Worked_Per_Week = st.number_input(
    "Average Hours Worked Per Week",
    min_value=0.0,
    value=40.0
)

Overtime_input = st.selectbox(
    "Overtime",
    ["No", "Yes"]
)

Overtime = 1 if Overtime_input == "Yes" else 0

st.markdown("---")

# Prediction Section
if st.button("Predict Attrition"):

    risk_score = 0

    # Rule-Based Prediction Logic
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

    # Results
    st.subheader("Prediction Result")

    if risk_score >= 3:
        st.error(
            "Prediction: Employee is likely to leave the company."
        )

    else:
        st.success(
            "Prediction: Employee is likely to stay in the company."
        )

    st.write(f"Risk Score: {risk_score} / 7")

    # Risk Interpretation
    if risk_score <= 2:
        st.info("Low Attrition Risk")

    elif risk_score <= 4:
        st.warning("Moderate Attrition Risk")

    else:
        st.error("High Attrition Risk")
