create database ibmsql;
use ibmsql;


SELECT COUNT(*) AS Total_Customers
FROM cleaned_ibm_churn; # when verifying 


SELECT *
FROM cleaned_ibm_churn
LIMIT 10;

SELECT COUNT(*) AS Total_Customers
FROM cleaned_ibm_churn;
SELECT COUNT(*) AS Churned_Customers
FROM cleaned_ibm_churn
WHERE Churn = 'Yes';


SELECT
ROUND(
SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
2
) AS Churn_Rate
FROM cleaned_ibm_churn;

SELECT
    Contract,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM cleaned_ibm_churn
GROUP BY Contract
ORDER BY Churn_Rate DESC;



SELECT
    PaymentMethod,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM cleaned_ibm_churn
GROUP BY PaymentMethod
ORDER BY Churn_Rate DESC;


SELECT
    InternetService,
    COUNT(*) AS Total_Customers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS Churned_Customers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS Churn_Rate
FROM cleaned_ibm_churn
GROUP BY InternetService
ORDER BY Churn_Rate DESC;


SELECT
    Churn,
    ROUND(AVG(tenure), 2) AS Average_Tenure
FROM cleaned_ibm_churn
GROUP BY Churn;


SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS Average_Monthly_Charges
FROM cleaned_ibm_churn
GROUP BY Churn;


SELECT
    customerID,
    MonthlyCharges,
    Contract,
    Churn
FROM cleaned_ibm_churn
ORDER BY MonthlyCharges DESC
LIMIT 5;







