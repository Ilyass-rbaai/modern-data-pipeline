SELECT
    ROUND(SUM(amount)::numeric, 2) AS total_revenue
FROM ecommerce.payments;