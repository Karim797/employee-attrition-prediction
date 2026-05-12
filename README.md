# Employee Attrition Prediction System

A modern end-to-end Machine Learning application built with Streamlit to analyze employee behavior, visualize workforce insights, and predict employee attrition risk using HR analytics and predictive modeling.

---

# 🌟 Overview

This project focuses on predicting whether an employee is likely to leave the company based on workplace satisfaction, performance indicators, compensation, and work-life balance factors.

The system combines:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning
- SMOTE balancing
- Streamlit Deployment

to create a professional AI-powered HR analytics platform.

---

# 🚀 Features

### 📊 Interactive EDA Dashboard
Explore:
- Attrition distribution
- Department patterns
- Gender analysis
- Salary distribution
- Missing values
- Workforce insights

### 🤖 Employee Attrition Prediction
Predict employee turnover risk using workplace and behavioral indicators.

### ⚖️ Imbalanced Data Handling
Implemented SMOTE to improve minority class prediction performance.

### 📈 Multiple ML Models
Compared several machine learning algorithms to select the best-performing model.

### 🎨 Professional Streamlit UI
Modern responsive interface with custom styling and multi-page navigation.

---

# 🛠️ Technology Stack

### Frontend
- Streamlit

### Data Analysis
- Pandas
- NumPy

### Visualization
- Plotly
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-Learn
- Imbalanced-Learn (SMOTE)

### Model Persistence
- Joblib

---

# 🤖 Machine Learning Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- AdaBoost
- Gradient Boosting

---

# 🏆 Final Model Selection

Gradient Boosting (SMOTE) achieved the highest Recall score of 0.98, making it highly effective at detecting employee attrition cases and delivering the strongest raw classification performance.

However, Logistic Regression (Tuned) was selected as the final deployed model due to its simpler architecture, better interpretability, lower computational cost, reduced risk of overfitting, and more stable real-world deployment performance on the imbalanced dataset.



---
## Acknowledgment

This project was developed as part of the Epsilon AI Data Science & Machine Learning Program.

Special thanks to the Epsilon AI team for the learning materials, project guidance, and mentorship throughout the program.

Main Epsilon AI Repository:
https://github.com/Epsilon-AI
---
# 📁 Project Structure

```bash
employee-attrition-prediction/
│
├── Home.py
├── pages/
│   ├── 1_EDA_Dashboard.py
│   └── 2_Employee_Attrition_Prediction.py
│
├── Employee_Attrition_ML_Project.ipynb
├── attrition_model.pkl
├── cleaned_employee_attrition.csv
├── requirements.txt
└── README.md
⚙️ Installation & Setup
Clone the repository
Bash
git clone https://github.com/yourusername/employee-attrition-prediction.git
Navigate to the project folder
Bash
cd employee-attrition-prediction
Install dependencies
Bash
pip install -r requirements.txt
Run the Streamlit application
Bash
streamlit run Home.py
📊 Dataset Information
The project uses an HR Employee Attrition dataset containing employee-related workplace and behavioral information.
Key Features Include:
👤 Employee Information
Age
Gender
Marital Status
Department
Job Role
💼 Job Information
Job Level
Monthly Income
Years at Company
Overtime
📈 Satisfaction & Performance
Job Satisfaction
Work Environment Satisfaction
Relationship with Manager
Work Life Balance
Absenteeism
🎯 Target Variable
Attrition
0 = Employee Stays
1 = Employee Leaves
📷 Streamlit Application
The deployed application includes:
🏠 Home Page
📊 EDA Dashboard
🤖 Attrition Prediction System
📌 Future Improvements
Deep Learning integration
Explainable AI (SHAP)
Employee recommendation system
Cloud deployment
Real-time HR analytics
👨‍💻 Author
Developed by Karim797
Dashboard Link [https://colab.research.google.com/drive/1wQwRJ_Ox6zbnLozD7DKYD9B8NfjWuAKm#scrollTo=bq93LInFGoRE](https://colab.research.google.com/drive/1wQwRJ_Ox6zbnLozD7DKYD9B8NfjWuAKm?usp=drive_link)
vedio link:
