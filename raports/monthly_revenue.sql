SELECT
    DATE_TRUNC('month', payment_date) AS month,
    ROUND(SUM(amount),2) AS revenue
FROM payments
GROUP BY month
ORDER BY month;