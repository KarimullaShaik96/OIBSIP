# Sales Prediction Using Python 📈

## OASIS INFOBYTE - Data Science Task 5

### 📌 Project Overview

This project uses machine learning regression techniques to predict sales
based on advertising expenditure.

The dataset contains advertising spending information for:

- TV
- Radio
- Newspaper

The target variable is Sales.

### 🎯 Objective

The objective of this project is to analyze the relationship between
advertising expenditure and sales and develop machine learning models
to predict sales.

### 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### 📂 Dataset

The project uses the Advertising dataset.

The main variables are:

- TV
- Radio
- Newspaper
- Sales

### 🔍 Exploratory Data Analysis

The project includes:

- Dataset inspection
- Missing-value analysis
- Duplicate-value analysis
- Descriptive statistics
- Advertising vs Sales scatter plots
- Correlation analysis
- Correlation heatmap

### ⚙️ Machine Learning

Three regression algorithms were implemented:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

### 📊 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model with the highest R² Score was selected as the best-performing
model.

### 🔮 Sales Prediction

The best-performing model was used to predict sales from a new advertising
budget containing TV, Radio, and Newspaper expenditure.

### 📈 Visualization

The project includes an Actual vs Predicted Sales visualization to compare
the model's predictions with the actual sales values.

### 📁 Project Structure

```text
Task-5-Sales-Prediction/
│
├── dataset/
│   └── Advertising.csv
│
├── Sales_Prediction.ipynb
├── README.md
├── requirements.txt
└── .gitkeep