SET search_path TO ecommerce;
ALTER TABLE orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES customers(customer_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

ALTER TABLE order_items
ADD CONSTRAINT fk_order_items_product
FOREIGN KEY (product_id)
REFERENCES products(product_id);

ALTER TABLE payments
ADD CONSTRAINT fk_payments_order
FOREIGN KEY (order_id)
REFERENCES orders(order_id);

CREATE INDEX idx_customer_email
ON customers(email);

CREATE INDEX idx_orders_customer
ON orders(customer_id);

CREATE INDEX idx_orders_date
ON orders(order_date);

CREATE INDEX idx_products_category
ON products(category);

CREATE INDEX idx_order_items_order
ON order_items(order_id);

CREATE INDEX idx_order_items_product
ON order_items(product_id);

CREATE INDEX idx_payment_order
ON payments(order_id);