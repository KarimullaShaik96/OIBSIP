# OIBSIP Data Analytics – Task 3: Data Cleaning

## 📌 Project Overview

This project demonstrates the process of cleaning and preparing a real-world dataset for analysis.

The Titanic passenger dataset was used to identify and handle common data quality problems such as missing values, duplicate records, inconsistent formatting, incorrect data types, and numerical outliers.

The cleaned dataset was saved as a separate CSV file for further analysis.

## 🎯 Objective

The main objective of this task is to demonstrate professional data cleaning skills by transforming a raw dataset into a clean and analysis-ready dataset.

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## 📂 Dataset

Dataset used:

**Titanic Dataset – Kaggle**

The dataset contains information about passengers aboard the Titanic, including passenger ID, survival status, passenger class, name, gender, age, ticket, fare, cabin, and embarkation port.

The original raw dataset is stored in:

```text
dataset/messy_dataset.csv
```

## 🔍 Data Cleaning Steps

The following data cleaning techniques were performed:

### 1. Data Quality Report

The dataset was inspected for:

* Number of rows and columns
* Missing values
* Duplicate records
* Data types
* Minimum and maximum values
* Basic statistical information

### 2. Missing Value Handling

Missing values were handled according to the nature of each column:

* **Age:** Missing values were replaced with the median.
* **Embarked:** Missing values were replaced with the mode.
* **Cabin:** Missing values were replaced with `Unknown`.

### 3. Duplicate Removal

Duplicate records were identified using Pandas `duplicated()` and removed using `drop_duplicates()`.

### 4. Data Standardization

Text columns were standardized by:

* Removing leading and trailing spaces
* Standardizing gender values
* Converting embarkation values to a consistent format

### 5. Data Type Correction

Data types were corrected according to the meaning of each column.

For example:

* `PassengerId` was treated as a string identifier.
* Numerical columns were converted to appropriate numeric types.
* `Age` and `Fare` were converted to floating-point values.

The dataset does not contain a date column, so date-to-datetime conversion was not applicable.

### 6. Outlier Detection

The Interquartile Range (IQR) method was used to identify potential outliers in numerical columns such as:

* Age
* SibSp
* Parch
* Fare

The detected extreme values were retained because they can represent valid passenger observations rather than data-entry errors.

### 7. Before vs After Comparison

A comparison was performed to evaluate:

* Row count
* Missing values
* Duplicate records
* Data types

before and after cleaning.

### 8. Cleaned Dataset

The final cleaned dataset was exported as:

```text
cleaned_dataset.csv
```

## 📁 Project Structure

```text
Task-3/
│
├── dataset/
│   └── messy_dataset.csv
│
├── Data_Cleaning.ipynb
│
├── cleaned_dataset.csv
│
├── README.md
│
└── requirements.txt
```

## 📊 Key Outcomes

The cleaning process produced a more consistent and analysis-ready dataset by:

* Handling missing values
* Removing duplicate records
* Standardizing text values
* Correcting data types
* Detecting numerical outliers
* Documenting the cleaning decisions
* Exporting the cleaned dataset

## 🧠 Conclusion

Data cleaning is an important step in any data analytics project because the quality of the input data directly affects the reliability of analysis and insights.

This project demonstrates a systematic approach to identifying and resolving common data quality issues using Python and Pandas.

## 👨‍💻 Author

**Shaik Karimulla**

**OASIS INFOBYTE – Data Analytics Internship**
