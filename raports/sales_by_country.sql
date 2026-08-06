SELECT
    c.country,
    ROUND(SUM(pay.amount),2) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
JOIN payments pay
ON o.order_id = pay.order_id
GROUP BY c.country
ORDER BY revenue DESC;