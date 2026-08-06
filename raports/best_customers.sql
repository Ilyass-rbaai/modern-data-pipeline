SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    ROUND(SUM(pay.amount),2) AS total_spent
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments pay
ON pay.order_id = o.order_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_spent DESC
LIMIT 10;