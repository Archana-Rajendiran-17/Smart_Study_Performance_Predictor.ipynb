# Smart Study Performance Predictor

## Project Overview
The Smart Study Performance Predictor is a Machine Learning based application
that predicts students' academic performance using study-related parameters.
The project integrates data preprocessing, visualization, machine learning
models, evaluation, and Flask-based deployment.

This project is developed as a Capstone ML Project and is suitable for
portfolio showcase and interviews.

## Dataset
The dataset contains the following features:
- study_time: Hours spent studying per day
- sleep_hours: Average sleep hours
- attendance: Attendance percentage
- test_score: Final exam score

A derived label `performance_level` is created with three classes:
- Low
- Medium
- High

## Machine Learning Models
- Random Forest Classifier: Predicts performance level
- Linear Regression: Predicts final test score

## Project Features
- Data preprocessing and feature scaling
- Data visualization
- Classification and regression models
- Model evaluation using Accuracy and RMSE
- Flask REST API for predictions

## How to Run the Project
1. Install required libraries:
   pip install -r requirements.txt

2. Run the Flask application:
   python app.py

3. Send a POST request to `/predict` with JSON input:
   {
     "study_time": 3,
     "sleep_hours": 7,
     "attendance": 85
   }

## Output
- Predicted test score
- Predicted performance level

## Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Flask
- Google Colab
- GitHub

## Author
Student Name
