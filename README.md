# Employee Attrition Prediction System

A modern end-to-end Machine Learning application built with Streamlit to analyze employee behavior, visualize workforce insights, and predict employee attrition risk using HR analytics and predictive modeling.

---

# 🌟 Overview

This project predicts whether an employee is likely to leave the company based on workplace satisfaction, performance indicators, compensation, and work-life balance factors.

The system combines:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning
- SMOTE for imbalanced data handling
- Streamlit deployment

to create a professional AI-powered HR analytics platform.

---

# 🚀 Features

## 📊 Interactive EDA Dashboard
Explore:
- Attrition distribution
- Department analysis
- Gender insights
- Salary distribution
- Missing values overview
- Workforce behavior patterns

## 🤖 Employee Attrition Prediction
Predict employee turnover risk using workplace and behavioral indicators.

## ⚖️ Imbalanced Data Handling
Implemented SMOTE to improve prediction performance for the minority class.

## 📈 Multiple Machine Learning Models
Compared multiple machine learning models to identify the best-performing solution.

## 🎨 Professional Streamlit UI
Modern responsive multi-page interface with clean navigation.

---

# 🛠️ Technology Stack

## Frontend
- Streamlit

## Data Analysis
- Pandas
- NumPy

## Visualization
- Plotly
- Matplotlib
- Seaborn

## Machine Learning
- Scikit-Learn
- Imbalanced-Learn (SMOTE)

## Model Persistence
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

**Logistic Regression with SMOTE** was selected as the final deployment model because it provided the best overall balance between **Recall and F1-score** for this imbalanced employee attrition classification problem.

Although **Decision Tree** achieved a higher Recall score, Logistic Regression with SMOTE demonstrated more stable and balanced performance, making it a more reliable choice.

Additionally, it offers:

- Better interpretability
- Lower risk of overfitting
- Faster prediction speed
- Lower computational cost
- Better suitability for real-world HR deployment

---

# 🙏 Acknowledgment

This project was developed as part of the **Epsilon AI Data Science & Machine Learning Program**.

Special thanks to the Epsilon AI team for the learning materials, project guidance, and mentorship.

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
```

---

# ⚙️ Installation & Setup

## Clone the repository
```bash
git clone https://github.com/yourusername/employee-attrition-prediction.git
```

## Navigate to the project folder
```bash
cd employee-attrition-prediction
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run the application
```bash
streamlit run Home.py
```

---

# 📊 Dataset Information

The project uses an HR Employee Attrition dataset containing employee workplace and behavioral data.

## 👤 Employee Information
- Age
- Gender
- Marital Status
- Department
- Job Role

## 💼 Job Information
- Job Level
- Monthly Income
- Years at Company
- Overtime

## 📈 Satisfaction & Performance
- Job Satisfaction
- Work Environment Satisfaction
- Relationship with Manager
- Work Life Balance
- Absenteeism

## 🎯 Target Variable
**Attrition**
- 0 = Employee Stays
- 1 = Employee Leaves

---

# 📷 Streamlit Application

The deployed application includes:

- 🏠 Home Page
- 📊 EDA Dashboard
- 🤖 Employee Attrition Prediction System

---

# 📌 Future Improvements

- Deep Learning integration
- Explainable AI (SHAP)
- Employee recommendation system
- Cloud deployment
- Real-time HR analytics

---

# 👨‍💻 Author

Developed by **Karim Deheya**
---

# 🔗 Project Links

🔗 [Live Dashboard](https://employee-attrition-prediction-zjeapazbjm2du7jthbkddr.streamlit.app/Employee_Attrition_Prediction)

📓 [Google Colab Notebook](https://colab.research.google.com/drive/1k13CKNsvGHIc7JR00XD_SaZIRWCP9qvm)

🎥 [Video Demo](https://drive.google.com/file/d/1z0UB8xs0aFASncC_oeWZdBcLZ5JTlPej/view?usp=drive_link)
