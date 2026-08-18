import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, ttest_ind


df = pd.read_csv("ibm churn.csv")
# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")

"""print("Dataset loaded successfully")
print("Shape:", df.shape)"""

# Test 1: Contract Type vs Churn

contract_table = pd.crosstab(df["Contract"], df["Churn"])

chi2, p_value, dof, expected = chi2_contingency(contract_table)

print("\nContract Type vs Churn")
print(contract_table)
print("Chi-square statistic:", chi2)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant association between Contract Type and Churn.")
else:
    print("Result: No statistically significant association between Contract Type and Churn.")

# Test 2: Internet Service vs Churn

internet_table = pd.crosstab(df["InternetService"], df["Churn"])

chi2, p_value, dof, expected = chi2_contingency(internet_table)

print("\nInternet Service vs Churn")
print(internet_table)
print("Chi-square statistic:", chi2)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant association between Internet Service and Churn.")
else:
    print("Result: No statistically significant association between Internet Service and Churn.")


# Test 3: Payment Method vs Churn

payment_table = pd.crosstab(df["PaymentMethod"], df["Churn"])

chi2, p_value, dof, expected = chi2_contingency(payment_table)

print("\nPayment Method vs Churn")
print(payment_table)
print("Chi-square statistic:", chi2)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant association between Payment Method and Churn.")
else:
    print("Result: No statistically significant association between Payment Method and Churn.")


# Test 4: Tenure vs Churn

tenure_no = df[df["Churn"] == "No"]["tenure"]
tenure_yes = df[df["Churn"] == "Yes"]["tenure"]

t_stat, p_value = ttest_ind(tenure_no, tenure_yes)

print("\nTenure vs Churn")
print("Average tenure - No Churn:", tenure_no.mean())
print("Average tenure - Churn:", tenure_yes.mean())
print("T-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant difference in tenure between churn groups.")
else:
    print("Result: No statistically significant difference in tenure between churn groups.")



# Test 5: Monthly Charges vs Churn

charges_no = df[df["Churn"] == "No"]["MonthlyCharges"]
charges_yes = df[df["Churn"] == "Yes"]["MonthlyCharges"]

t_stat, p_value = ttest_ind(charges_no, charges_yes)

print("\nMonthly Charges vs Churn")
print("Average monthly charges - No Churn:", charges_no.mean())
print("Average monthly charges - Churn:", charges_yes.mean())
print("T-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant difference in monthly charges between churn groups.")
else:
    print("Result: No statistically significant difference in monthly charges between churn groups.")


# Test 6: Total Charges vs Churn

total_charges_no = df[df["Churn"] == "No"]["TotalCharges"].dropna()
total_charges_yes = df[df["Churn"] == "Yes"]["TotalCharges"].dropna()

t_stat, p_value = ttest_ind(total_charges_no, total_charges_yes)

print("\nTotal Charges vs Churn")
print("Average total charges - No Churn:", total_charges_no.mean())
print("Average total charges - Churn:", total_charges_yes.mean())
print("T-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Statistically significant difference in total charges between churn groups.")
else:
    print("Result: No statistically significant difference in total charges between churn groups.")



# FEATURE ENGINEERING

# Create a separate dataset for Machine Learning

ml_df = df.copy()
print("\nML Dataset Shape:", ml_df.shape)
print(ml_df.head())

# Check ML dataset columns and data types

print("\nML Dataset Columns and Data Types:")
print(ml_df.dtypes)

# Remove customer ID because it is an identifier, not a predictive feature
ml_df = ml_df.drop("customerID", axis=1)

print("\nColumns after removing customerID:")
print(ml_df.columns)

# Separate features (X) and target (y)

X = ml_df.drop("Churn", axis=1)
y = ml_df["Churn"]

print("\nFeatures (X) shape:", X.shape)
print("Target (y) shape:", y.shape)
print("\nTarget values:")
print(y.value_counts())

# Convert Churn into binary values

y = y.map({"No": 0, "Yes": 1})

print("\nEncoded target values:")
print(y.value_counts())

# Encode categorical features using One-Hot Encoding

X = pd.get_dummies(X, drop_first=True)

print("\nEncoded Features Shape:", X.shape)
print("\nEncoded Feature Columns:")
print(X.columns)

# Handle missing values in TotalCharges
X["TotalCharges"] = X["TotalCharges"].fillna(X["TotalCharges"].median())

print("\nMissing values after handling:")
print(X.isnull().sum().sum())


#train split test 
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nScaled training data shape:", X_train_scaled.shape)
print("Scaled testing data shape:", X_test_scaled.shape)

# LOGISTIC REGRESSION

# LOGISTIC REGRESSION

from sklearn.linear_model import LogisticRegression

logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

logistic_model.fit(X_train_scaled, y_train)

print("\nLogistic Regression model trained successfully.")




# RANDOM FOREST

from sklearn.ensemble import RandomForestClassifier

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully.")


# MODEL PREDICTIONS

# Logistic Regression predictions
y_pred_logistic = logistic_model.predict(X_test_scaled)
y_prob_logistic = logistic_model.predict_proba(X_test_scaled)[:, 1]

# Random Forest predictions
y_pred_rf = random_forest_model.predict(X_test)
y_prob_rf = random_forest_model.predict_proba(X_test)[:, 1]

print("\nPredictions generated successfully.")




# MODEL EVALUATION

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)

# Logistic Regression metrics
logistic_accuracy = accuracy_score(y_test, y_pred_logistic)
logistic_precision = precision_score(y_test, y_pred_logistic)
logistic_recall = recall_score(y_test, y_pred_logistic)
logistic_f1 = f1_score(y_test, y_pred_logistic)
logistic_roc_auc = roc_auc_score(y_test, y_prob_logistic)
logistic_cm = confusion_matrix(y_test, y_pred_logistic)

# Random Forest metrics
rf_accuracy = accuracy_score(y_test, y_pred_rf)
rf_precision = precision_score(y_test, y_pred_rf)
rf_recall = recall_score(y_test, y_pred_rf)
rf_f1 = f1_score(y_test, y_pred_rf)
rf_roc_auc = roc_auc_score(y_test, y_prob_rf)
rf_cm = confusion_matrix(y_test, y_pred_rf)

# Print results
print("\n===== LOGISTIC REGRESSION =====")
print("Accuracy:", logistic_accuracy)
print("Precision:", logistic_precision)
print("Recall:", logistic_recall)
print("F1-Score:", logistic_f1)
print("ROC-AUC:", logistic_roc_auc)
print("Confusion Matrix:")
print(logistic_cm)

print("\n===== RANDOM FOREST =====")
print("Accuracy:", rf_accuracy)
print("Precision:", rf_precision)
print("Recall:", rf_recall)
print("F1-Score:", rf_f1)
print("ROC-AUC:", rf_roc_auc)
print("Confusion Matrix:")
print(rf_cm)



# STEP 13 — FEATURE IMPORTANCE

# Logistic Regression Feature Importance

logistic_importance = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": logistic_model.coef_[0]
})

# Calculate absolute importance
logistic_importance["Absolute_Importance"] = (
    logistic_importance["Coefficient"].abs()
)

# Sort by importance
logistic_importance = logistic_importance.sort_values(
    by="Absolute_Importance",
    ascending=False
)

print("\n===== LOGISTIC REGRESSION FEATURE IMPORTANCE =====")
print(logistic_importance.head(15))



# Random Forest Feature Importance

rf_importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": random_forest_model.feature_importances_
})

rf_importance = rf_importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n===== RANDOM FOREST FEATURE IMPORTANCE =====")
print(rf_importance.head(15))
