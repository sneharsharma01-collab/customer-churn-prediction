import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# STEP 1 : DATA QUALITY CHECK AND CLEANING 


df = pd.read_csv("ibm churn.csv")
# cols n starting 10 data 
print(df.head(10))

#check no. of rows n cols
print(df.shape)

# Display all column names
print("Columns in the Dataset:\n")

for column in df.columns:
    print(column)


# Check missing values in each column
print("Missing Values in Each Column:\n")
print(df.isnull().sum())

# Check blank values in each column
print("Blank Values in Each Column:\n")
print((df == " ").sum())

# Convert TotalCharges to Numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

print("Data Type of TotalCharges after Conversion:")
print(df["TotalCharges"].dtype)



# Check Missing Values Again
print("Missing Values After Conversion:\n")
print(df.isnull().sum())

# Check duplicate rows
print("Number of Duplicate Rows:")
print(df.duplicated().sum())



# Check data types of columns
print("Data Types of Columns:\n")
print(df.dtypes)


# Check missing values in TotalCharges
print("Missing TotalCharges Values:")
print(df["TotalCharges"].isnull().sum())


# Fill missing TotalCharges with median value
df["TotalCharges"] = df["TotalCharges"].fillna(df["TotalCharges"].median())

# Check missing values again
print("Missing Values After Filling TotalCharges:\n")
print(df.isnull().sum())

# Final Data Quality Check
print("Final Missing Values:")
print(df.isnull().sum().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

# Dataset Information
print(df.info())

# Statistical Summary
print(df.describe())

# STEP 2 EDA 
print(df["Churn"].value_counts())

# Calculate Churn Percentage
churn_percentage = df["Churn"].value_counts(normalize=True) * 100

print(churn_percentage)

# Churn count by gender
print(pd.crosstab(df["gender"], df["Churn"]))

# Churn Analysis by Contract Type
contract_churn_rate = pd.crosstab(
    df["Contract"], 
    df["Churn"], 
    normalize="index"
) * 100

print(contract_churn_rate)
#Contract type is one of the strongest churn indicators. 
# Customers on month-to-month contracts have a churn rate of 42.7%, compared to only 2.8% for two-year contracts. 
# This suggests that encouraging customers to move towards longer-term contracts may improve retention.

# Average Tenure by Churn
print("\nAverage Tenure by Churn:")
print(df.groupby("Churn")["tenure"].mean())
#Tenure appears to be an important churn factor. "
#ustomers who remain with the company have an average tenure of 37.6 months, whereas churned customers leave after approximately 18 months."
#This highlights the importance of improving early customer experience and retention strategies."


# Average Monthly Charges by Churn
print("\nAverage Monthly Charges by Churn:")
print(df.groupby("Churn")["MonthlyCharges"].mean())
#Monthly charges show a relationship with churn. "
#Customers who churn have higher average monthly charges than retained customers, indicating that pricing and perceived value may influence customer retention."

#Churn by Payment Method
payment_churn_rate = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize="index"
) * 100

print(payment_churn_rate)
#Payment method analysis indicates that electronic check users have significantly higher churn compared to customers using automatic payment methods. 
#This suggests that encouraging automatic payment adoption may help improve customer retention."


# Churn percentage by Internet Service
print("\nInternet Service Churn Rate:")
print(
    pd.crosstab(
        df["InternetService"], 
        df["Churn"], 
        normalize="index"
    ) * 100
)




#STEP 3 : DATA VISUALIZATION

# Chart 1 : Customer Churn Distribution

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="Churn")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")

plt.savefig("visuals/churn_distribution.png", dpi=300, bbox_inches="tight")

plt.show()


# Chart 2 : Contract Type vs Churn

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="Contract", hue="Churn")

plt.title("Contract Type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")

plt.legend(title="Churn")

plt.savefig("visuals/contract_vs_churn.png", dpi=300, bbox_inches="tight")

plt.show()


# Chart 3 : Tenure vs Churn

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="Churn", y="tenure")

plt.title("Customer Tenure by Churn Status")
plt.xlabel("Churn Status")
plt.ylabel("Tenure (Months)")

plt.savefig("visuals/tenure_vs_churn.png", dpi=300, bbox_inches="tight")

plt.show()


# Chart 4 : Monthly Charges vs Churn

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="Churn", y="MonthlyCharges")

plt.title("Monthly Charges by Churn Status")
plt.xlabel("Churn Status")
plt.ylabel("Monthly Charges")

plt.savefig("visuals/monthlycharges_vs_churn.png", dpi=300, bbox_inches="tight")

plt.show()


# Chart 5: Payment Method vs Churn

plt.figure(figsize=(11,6))

sns.countplot(
    data=df,
    x="PaymentMethod",
    hue="Churn"
)

plt.title("Customer Churn by Payment Method", fontsize=16, pad=20)
plt.xlabel("Payment Method", fontsize=12, labelpad=15)
plt.ylabel("Number of Customers", fontsize=12, labelpad=15)

plt.xticks(
    rotation=25,
    ha="right",
    fontsize=11
)

plt.legend(title="Churn", loc="upper right")

plt.tight_layout(pad=2)

plt.savefig(
    "visuals/paymentmethod_vs_churn.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Chart 6: Internet Service vs Churn
plt.figure(figsize=(10,6))

sns.countplot(
    data=df,
    x="InternetService",
    hue="Churn"
)

plt.title("Customer Churn by Internet Service", fontsize=16, pad=20)
plt.xlabel("Internet Service", fontsize=12, labelpad=15)
plt.ylabel("Number of Customers", fontsize=12, labelpad=15)

plt.xticks(fontsize=11)

plt.legend(title="Churn", loc="upper right")

plt.tight_layout(pad=2)

plt.savefig(
    "visuals/internetservice_vs_churn.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()




#STEP 4 : CORRELATION ANALYSIS 

plt.figure(figsize=(8,6))

correlation = df.select_dtypes(include=np.number).corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Numerical Features", fontsize=16, pad=20)

plt.tight_layout()

plt.savefig(
    "visuals/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# STEP 5: Key Business Insights

"""
1. Customer Churn Overview:
- The overall churn rate is approximately 26.54%, indicating that around one-fourth of customers leave the service.

2. Contract Impact:
- Month-to-month contract customers have the highest churn rate (~42.7%).
- Long-term contract customers show significantly lower churn, especially two-year contracts (~2.8% churn).

3. Customer Tenure:
- Customers who churn have a lower average tenure (~18 months) compared to retained customers (~38 months).
- Early customer engagement and onboarding improvements may reduce churn.

4. Pricing Impact:
- Customers who churn have higher average monthly charges compared to retained customers.
- Pricing strategy and perceived value may influence customer retention.

5. Payment Method:
- Customers using electronic checks show higher churn compared to automatic payment methods.
- Encouraging automatic payments may improve customer retention.

6. Internet Service:
- Fiber optic customers show higher churn compared to DSL and customers without internet service.
- Service quality, pricing, or customer expectations should be investigated.

7. Overall Recommendation:
- Focus retention efforts on new customers, month-to-month contract users,
  high monthly charge customers, and electronic check users.
"""


df.to_csv("cleaned_ibm_churn.csv", index=False)

print("Cleaned dataset exported successfully!")










