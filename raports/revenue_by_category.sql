SELECT
    p.category,
    ROUND(SUM(oi.quantity * oi.price),2) AS revenue
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;