SELECT
    DATE_TRUNC('month', payment_date) AS month,
    ROUND(SUM(amount)::numeric, 2) AS revenue
FROM ecommerce.payments
GROUP BY DATE_TRUNC('month', payment_date)
ORDER BY month;