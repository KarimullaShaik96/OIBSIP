# Customer Segmentation Analysis

## OASIS INFOBYTE Internship — Data Analytics Task 2

### Objective

The objective of this project is to segment an e-commerce company's customers based on their purchasing behavior. Customer segmentation helps businesses understand different customer groups and develop targeted marketing strategies.

## Dataset

The **Online Retail Dataset** was used for this project.

The dataset contains transactional information such as:

* Invoice Number
* Stock Code
* Product Description
* Quantity
* Invoice Date
* Unit Price
* Customer ID
* Country

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Jupyter Notebook

## Methodology

### 1. Data Loading and Cleaning

The dataset was loaded and cleaned by:

* Removing missing Customer IDs
* Removing cancelled transactions
* Removing invalid quantities
* Removing invalid unit prices
* Converting dates and numerical columns to appropriate data types

### 2. RFM Analysis

Three important customer behavior features were calculated:

* **Recency** — How recently a customer made a purchase
* **Frequency** — How frequently a customer makes purchases
* **Monetary** — How much money a customer spends

### 3. Feature Standardization

The RFM features were standardized using `StandardScaler` so that the features could be compared fairly during clustering.

### 4. K-Means Clustering

The K-Means clustering algorithm was applied to group customers based on their purchasing behavior.

The **Elbow Method** was used to identify a suitable number of clusters.

### 5. Visualization

Customer segments were visualized using:

* Recency vs Frequency
* Frequency vs Monetary
* Recency vs Monetary

A bar chart was also created to show the number of customers in each cluster.

## Customer Segments

The analysis identifies different customer groups based on their purchasing behavior, such as:

* VIP Customers
* Loyal Customers
* At-Risk High Value Customers
* Occasional Customers

## Marketing Recommendations

### VIP Customers

* Provide exclusive rewards
* Offer loyalty benefits
* Give early access to products
* Provide personalized recommendations

### Loyal Customers

* Encourage repeat purchases
* Offer loyalty points
* Provide bundle offers
* Send personalized recommendations

### At-Risk High Value Customers

* Send re-engagement campaigns
* Provide limited-time discounts
* Recommend previously purchased products
* Encourage customers to return

### Occasional Customers

* Provide promotional offers
* Encourage repeat purchases
* Send relevant product recommendations
* Introduce loyalty programs

## Key Insights

* RFM analysis helps identify differences in customer purchasing behavior.
* K-Means clustering can group customers with similar purchasing patterns.
* Recency, Frequency, and Monetary value are useful features for customer segmentation.
* High-value customers can be targeted with loyalty and retention strategies.
* At-risk customers can be targeted with re-engagement campaigns.
* Occasional customers can be encouraged to increase their purchase frequency.

## Conclusion

Customer segmentation provides businesses with a better understanding of their customers. The RFM-based K-Means approach used in this project creates meaningful customer groups that can support targeted marketing, improve customer retention, and increase business revenue.
