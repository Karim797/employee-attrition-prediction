import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load trained model
model = joblib.load('attrition_model.pkl')

# Page configuration
st.set_page_config(
    page_title="Employee Attrition Prediction",
    page_icon="📊",
    layout="centered"
)

# Title
st.title(" Employee Attrition Prediction App")

st.write(
    "This application predicts whether an employee is likely to leave the company "
    "based on HR-related features."
)

st.markdown("---")

# Employee Information
st.header("Employee Information")

Age = st.number_input("Age", min_value=18, max_value=65, value=30)

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
    "Job Level",
    1, 5, 2
)

Monthly_Income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=10000.0
)

Hourly_Rate = st.number_input(
    "Hourly Rate",
    min_value=0.0,
    value=50.0
)

Years_at_Company = st.number_input(
    "Years at Company",
    min_value=0.0,
    value=3.0
)

Years_in_Current_Role = st.number_input(
    "Years in Current Role",
    min_value=0.0,
    value=2.0
)

Years_Since_Last_Promotion = st.number_input(
    "Years Since Last Promotion",
    min_value=0.0,
    value=1.0
)

Work_Life_Balance = st.slider(
    "Work Life Balance",
    1, 4, 3
)

Job_Satisfaction = st.slider(
    "Job Satisfaction",
    1, 5, 3
)

Performance_Rating = st.slider(
    "Performance Rating",
    1, 4, 3
)

Training_Hours_Last_Year = st.number_input(
    "Training Hours Last Year",
    min_value=0.0,
    value=40.0
)

Project_Count = st.number_input(
    "Project Count",
    min_value=0.0,
    value=5.0
)

Distance_From_Home = st.number_input(
    "Distance From Home",
    min_value=0.0,
    value=10.0
)

Absenteeism = st.number_input(
    "Absenteeism",
    min_value=0.0,
    value=5.0
)

Average_Hours_Worked_Per_Week = st.number_input(
    "Average Hours Worked Per Week",
    min_value=0.0,
    value=40.0
)

Work_Environment_Satisfaction = st.slider(
    "Work Environment Satisfaction",
    1, 4, 3
)

Relationship_with_Manager = st.slider(
    "Relationship with Manager",
    1, 4, 3
)

Job_Involvement = st.slider(
    "Job Involvement",
    1, 4, 3
)

Number_of_Companies_Worked = st.number_input(
    "Number of Companies Worked",
    min_value=0.0,
    value=2.0
)

Overtime_input = st.selectbox(
    "Overtime",
    ["No", "Yes"]
)

Overtime = 1 if Overtime_input == "Yes" else 0

# Feature Engineering
Monthly_Income_Log = np.log1p(Monthly_Income)

Overall_Satisfaction = round(
    (
        Job_Satisfaction
        + Work_Environment_Satisfaction
        + Relationship_with_Manager
    ) / 3,
    2
)

Promotion_Wait_Ratio = (
    Years_Since_Last_Promotion /
    (Years_at_Company + 1)
)

Income_Per_Level = round(
    Monthly_Income_Log / (Job_Level + 1),
    2
)

# Create input dataframe
input_data = pd.DataFrame([{
    "Age": Age,
    "Job_Level": Job_Level,
    "Monthly_Income": Monthly_Income_Log,
    "Hourly_Rate": Hourly_Rate,
    "Years_at_Company": Years_at_Company,
    "Years_in_Current_Role": Years_in_Current_Role,
    "Years_Since_Last_Promotion": Years_Since_Last_Promotion,
    "Work_Life_Balance": Work_Life_Balance,
    "Job_Satisfaction": Job_Satisfaction,
    "Performance_Rating": Performance_Rating,
    "Training_Hours_Last_Year": Training_Hours_Last_Year,
    "Project_Count": Project_Count,
    "Distance_From_Home": Distance_From_Home,
    "Absenteeism": Absenteeism,
    "Average_Hours_Worked_Per_Week": Average_Hours_Worked_Per_Week,
    "Work_Environment_Satisfaction": Work_Environment_Satisfaction,
    "Relationship_with_Manager": Relationship_with_Manager,
    "Job_Involvement": Job_Involvement,
    "Number_of_Companies_Worked": Number_of_Companies_Worked,
    "Overtime": Overtime,
    "Overall_Satisfaction": Overall_Satisfaction,
    "Promotion_Wait_Ratio": Promotion_Wait_Ratio,
    "Income_Per_Level": Income_Per_Level,
    "Gender": Gender,
    "Marital_Status": Marital_Status,
    "Department": Department,
    "Job_Role": Job_Role
}])

st.markdown("---")

# Prediction Button
if st.button("Predict Attrition"):

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error(
            f"Employee is likely to leave the company.\\n\\n"
            f"Probability: {probability:.2%}"
        )
    else:
        st.success(
            f"Employee is likely to stay in the company.\\n\\n"
            f"Probability of leaving: {probability:.2%}"
        )

"""
