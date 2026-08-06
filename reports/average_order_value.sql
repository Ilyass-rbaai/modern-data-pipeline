SELECT
    ROUND(AVG(amount)::numeric, 2) AS average_order_value
FROM ecommerce.payments;