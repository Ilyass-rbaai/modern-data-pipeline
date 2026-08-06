ALTER TABLE ecommerce.orders
ADD CONSTRAINT fk_orders_customer
FOREIGN KEY (customer_id)
REFERENCES ecommerce.customers(customer_id);

ALTER TABLE ecommerce.order_items
ADD CONSTRAINT fk_order_items_order
FOREIGN KEY (order_id)
REFERENCES ecommerce.orders(order_id);

ALTER TABLE ecommerce.order_items
ADD CONSTRAINT fk_order_items_product
FOREIGN KEY (product_id)
REFERENCES ecommerce.products(product_id);

ALTER TABLE ecommerce.payments
ADD CONSTRAINT fk_payments_order
FOREIGN KEY (order_id)
REFERENCES ecommerce.orders(order_id);

CREATE INDEX idx_customer_email
ON ecommerce.customers(email);

CREATE INDEX idx_orders_customer
ON ecommerce.orders(customer_id);

CREATE INDEX idx_orders_date
ON ecommerce.orders(order_date);

CREATE INDEX idx_products_category
ON ecommerce.products(category);

CREATE INDEX idx_order_items_order
ON ecommerce.order_items(order_id);

CREATE INDEX idx_order_items_product
ON ecommerce.order_items(product_id);

CREATE INDEX idx_payment_order
ON ecommerce.payments(order_id);