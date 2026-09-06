# Car Price Prediction 🚗

## OASIS INFOBYTE - Data Science Task 3

### 📌 Project Overview

This project uses machine learning regression techniques to predict the selling
price of used cars.

The model uses information such as manufacturing year, present price,
kilometers driven, fuel type, transmission, ownership, and other available
vehicle attributes.

### 🎯 Objective

The objective of this project is to build machine learning regression models
that can predict used car selling prices and compare their performance.

### 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### 📂 Dataset

The project uses a car price dataset containing information about used cars.

Important attributes include:

- Car Name
- Year
- Selling Price
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner

### 🔍 Data Analysis

The project includes:

- Dataset inspection
- Missing-value analysis
- Duplicate-value analysis
- Descriptive statistics
- Selling-price distribution
- Present-price vs selling-price analysis
- Car age analysis
- Categorical feature analysis

### ⚙️ Data Preprocessing

The dataset was prepared for machine learning by:

- Cleaning column names
- Removing unnecessary columns
- Creating a Car Age feature
- Encoding categorical variables
- Separating features and target
- Splitting data into training and testing sets

### 🤖 Machine Learning Models

Three regression algorithms were implemented:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

### 📈 Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

The model with the highest R² Score was selected as the best-performing model.

### 📊 Prediction

The selected model was used to predict the selling price of a car.

Actual and predicted prices were compared to understand the model's
performance.

### 📁 Project Structure

```text
Task-3-Car-Price-Prediction/
│
├── dataset/
│   └── car data.csv
│
├── Car_Price_Prediction.ipynb
├── README.md
├── requirements.txt
└── .gitkeep
