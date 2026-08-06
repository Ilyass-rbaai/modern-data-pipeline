SELECT
    DATE(payment_date) AS day,
    ROUND(SUM(amount),2) AS revenue
FROM payments
GROUP BY day
ORDER BY day;