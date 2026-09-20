# Customer Churn Prediction

End-to-end customer churn analysis and prediction using Python, SQL, Machine Learning, and Power BI.

## Project Overview

This project analyzes customer churn using the IBM Telco Customer Churn dataset to identify factors associated with customer attrition and develop predictive models for churn.

The project combines Python, SQL, statistical analysis, machine learning, and Power BI to take the analysis from data preparation and exploratory analysis to predictive modeling and business recommendations.

The analysis focuses on factors such as contract type, tenure, internet service, payment method, and monthly charges to understand customer churn patterns and support data-driven retention strategies.

## Business Problem

Customer churn can reduce revenue and increase the cost of acquiring new customers. The objective of this project is to analyze customer-level data to identify patterns associated with churn and determine which customer characteristics and service factors are most strongly related to customer attrition.

The analysis examines factors such as contract type, tenure, internet service, payment method, and monthly charges to understand differences between customers who churn and those who remain.

## Objectives

* Analyze customer churn patterns using customer demographics, services, contracts, and billing information.
* Identify key factors associated with customer churn using statistical analysis.
* Perform SQL-based analysis to answer business questions related to customer retention.
* Build machine learning models to predict customer churn.
* Develop an interactive Power BI dashboard to communicate key findings.
* Provide data-driven recommendations that can support customer retention strategies.

## Tools & Technologies

* Python — Data cleaning, exploratory data analysis, statistical analysis, and machine learning
* SQL (MySQL) — Data analysis and business queries
* Power BI — Interactive dashboard and data visualization
* Pandas & NumPy — Data manipulation and preprocessing
* Matplotlib & Seaborn — Exploratory data visualization
* Scikit-learn — Machine learning model development and evaluation
* SciPy — Statistical hypothesis testing

## Data Preparation

The IBM Telco Customer Churn dataset contains 7,043 customer records and information related to customer demographics, services, contracts, and billing.

The data preparation process included:

* Handling missing values in the TotalCharges column.
* Converting TotalCharges to a numeric data type.
* Removing unnecessary columns that did not contribute to the analysis.
* Encoding categorical variables for statistical analysis and machine learning.
* Preparing the cleaned dataset for exploratory analysis, SQL analysis, statistical testing, and predictive modeling.

## Exploratory Data Analysis

Exploratory data analysis was performed to understand customer churn patterns and identify important differences between customers who churned and those who remained.

The analysis examined:

* Overall churn distribution
* Churn by contract type
* Churn by internet service
* Churn by payment method
* Customer tenure by churn status
* Monthly charges by churn status
* Customer and service characteristics associated with higher churn

The findings from EDA were used to guide the subsequent statistical analysis, SQL analysis, and machine learning stages.

## Statistical Analysis

Statistical hypothesis testing was used to evaluate whether observed differences in customer characteristics and service categories were statistically significant.

The analysis included:

* Independent samples t-test to compare customer tenure between churned and non-churned customers.
* Chi-square tests to examine the relationship between churn and categorical variables such as contract type, internet service, and payment method.

The statistical results showed significant relationships between churn and several customer and service factors, supporting further analysis through machine learning models.

## Machine Learning

Machine learning models were developed to predict whether a customer is likely to churn based on customer and service-related features.

The following models were evaluated:

* Logistic Regression
* Random Forest Classifier

### Model Performance

| Model               | Accuracy | F1 Score | ROC-AUC |
| ------------------- | -------: | -------: | ------: |
| Logistic Regression |    80.7% |    60.9% |   84.2% |
| Random Forest       |    78.6% |        — |   82.5% |

Logistic Regression achieved a ROC-AUC of 0.842, while Random Forest achieved a ROC-AUC of 0.825. These results were used to evaluate the models' ability to distinguish between customers who churned and those who remained.

## SQL Analysis

SQL analysis was performed using MySQL to investigate customer churn patterns and answer business-focused questions.

The analysis included:

* Churn distribution across different customer segments.
* Churn rates by contract type.
* Churn patterns across internet service and payment methods.
* Comparison of customer tenure and monthly charges across churn groups.
* Aggregation and filtering of customer-level data to identify patterns relevant to retention.

The SQL analysis provided additional business insights and complemented the findings from Python, statistical analysis, and machine learning.

## Power BI Dashboard

An interactive Power BI dashboard was developed to monitor customer churn and identify key retention patterns.

The dashboard includes:

* Total Customers
* Total Churned Customers
* Churn Rate
* Average Monthly Charges
* Average Tenure
* Churn analysis by Contract, Internet Service, and Payment Method
* Comparison of Average Tenure and Monthly Charges by Churn Status
* Interactive slicers for Churn, Contract, Internet Service, and Payment Method

### Dashboard Preview

![Customer Churn Dashboard](ss%20ibm.png)

## Key Insights

The analysis identified several notable patterns associated with customer churn:

* Overall churn rate was approximately 26.5% across 7,043 customers.
* Month-to-month contract customers had substantially higher churn than customers on one-year or two-year contracts.
* Customers who churned had a lower average tenure of approximately 18 months compared with approximately 38 months for customers who remained.
* Customers who churned had higher average monthly charges of approximately 74.44 compared with 61.27 for customers who remained.
* Electronic check customers showed a higher churn rate compared with several other payment methods.
* Fiber optic customers showed a higher churn rate compared with other internet service categories.
* Statistical testing indicated significant relationships between churn and contract type, internet service, payment method, and customer tenure.

## Business Recommendations

Based on the analysis, the following retention strategies can be considered:

* Encourage longer-term contracts through targeted plans, incentives, or retention offers.
* Identify month-to-month customers with high-risk characteristics for proactive retention campaigns.
* Monitor customers with higher monthly charges and assess opportunities for personalized offers or service optimization.
* Investigate churn patterns among electronic check customers and evaluate whether alternative payment options or targeted engagement could improve retention.
* Review the experience of fiber optic customers to identify service, pricing, or support factors associated with higher churn.
* Use the predictive model to help prioritize customers for targeted retention efforts.

