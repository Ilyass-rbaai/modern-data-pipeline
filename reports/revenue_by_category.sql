SELECT
    p.category,
    ROUND(SUM(pay.amount)::numeric, 2) AS total_revenue
FROM ecommerce.products p
JOIN ecommerce.order_items oi
    ON p.product_id = oi.product_id
JOIN ecommerce.orders o
    ON oi.order_id = o.order_id
JOIN ecommerce.payments pay
    ON o.order_id = pay.order_id
GROUP BY p.category
ORDER BY total_revenue DESC;