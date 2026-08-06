SELECT
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold,
    ROUND(SUM(oi.quantity * oi.price)::numeric, 2) AS total_revenue
FROM ecommerce.order_items oi
JOIN ecommerce.products p
    ON oi.product_id = p.product_id
GROUP BY
    p.product_name
ORDER BY
    total_revenue DESC
LIMIT 10;