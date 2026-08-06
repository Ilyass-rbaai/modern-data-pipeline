CREATE OR REPLACE VIEW sales_report AS
SELECT
    o.order_id,
    o.order_date,
    c.customer_id,
    c.first_name,
    c.last_name,
    c.country,
    p.product_name,
    p.category,
    oi.quantity,
    oi.price,
    pay.amount
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN order_items oi
    ON o.order_id = oi.order_id
JOIN products p
    ON oi.product_id = p.product_id
JOIN payments pay
    ON o.order_id = pay.order_id;