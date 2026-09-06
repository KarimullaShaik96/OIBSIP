# Email Spam Detection 📧

## OASIS INFOBYTE - Data Science Task 4

### 📌 Project Overview

This project uses Natural Language Processing (NLP) and machine learning
techniques to classify messages as either spam or legitimate (ham).

### 🎯 Objective

The objective is to build a machine learning model that can automatically
identify spam messages from their text content.

### 🛠️ Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TF-IDF

### 📂 Dataset

The project uses a spam message dataset containing two main categories:

- Ham — legitimate messages
- Spam — unwanted messages

### 🔍 Exploratory Data Analysis

The project includes:

- Dataset inspection
- Missing-value analysis
- Spam vs Ham distribution
- Message-length analysis
- Visualization of message characteristics

### ⚙️ Text Preprocessing

The message text was converted into numerical features using
TF-IDF (Term Frequency-Inverse Document Frequency).

### 🤖 Machine Learning Models

Two classification algorithms were implemented:

1. Multinomial Naive Bayes
2. Logistic Regression

### 📈 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

The best-performing model was selected based on its F1-score.

### 🧪 Prediction

The selected model was tested using new sample messages and classified
them as either:

- SPAM
- HAM

### 📁 Project Structure

```text
Task-4-Email-Spam-Detection/
│
├── dataset/
│   └── spam.csv
│
├── Email_Spam_Detection.ipynb
├── README.md
├── requirements.txt
└── .gitkeep
