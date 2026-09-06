# Retail Sales Analysis

## OASIS INFOBYTE – Data Analytics Task 1

### Project Overview

This project performs exploratory data analysis on a retail sales dataset to identify important sales trends, customer purchasing patterns, and product category performance.

The analysis was performed using Python and popular data analysis and visualization libraries.

## Objectives

* Analyze overall retail sales performance.
* Identify monthly sales trends.
* Compare sales across product categories.
* Analyze sales by gender.
* Study purchasing behavior across different age groups.
* Identify frequent customers.
* Analyze quantity sold and average transaction value.
* Identify the best-performing product category.
* Generate useful business insights through visualizations.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Jupyter Notebook

## Dataset

The project uses a retail sales transaction dataset containing information such as:

* Transaction ID
* Date
* Customer ID
* Gender
* Age
* Product Category
* Quantity
* Price per Unit
* Total Amount

The dataset is stored in the `dataset` folder.

## Analysis Performed

### 1. Data Loading and Cleaning

The dataset was loaded using Pandas. Column names were cleaned, dates were converted to datetime format, and missing records were removed.

### 2. Exploratory Data Analysis

The dataset was examined using descriptive statistics, data types, missing-value analysis, and duplicate-value checks.

### 3. Monthly Sales Analysis

Monthly sales were calculated and visualized to understand sales trends over time.

### 4. Product Category Analysis

Product categories were compared based on total sales, quantity sold, average purchase amount, and number of transactions.

### 5. Customer Demographic Analysis

Sales were analyzed by gender and age group to understand customer purchasing patterns.

### 6. Customer Transaction Analysis

Customer transaction frequency was analyzed to identify frequent customers.

### 7. Business Insights

The project identifies the highest-performing product category, highest-spending age group, higher-sales gender group, and highest-value transaction.

## Project Structure

```text
Task-1-Retail-Sales/
│
├── dataset/
│   └── retail_sales_dataset.csv
│
├── Retail_Sales_Analysis.ipynb
├── README.md
└── requirements.txt
```

## Conclusion

The Retail Sales Analysis project demonstrates how Python can be used to explore retail transaction data and generate meaningful business insights.

The analysis covers sales trends, product performance, customer demographics, transaction frequency, and purchasing behavior. The resulting insights can help businesses understand customer demand and support data-driven decision-making.
