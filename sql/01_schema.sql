CREATE TABLE customers(
    customer_id VARCHAR(50) PRIMARY KEY,
    customer_unique_id VARCHAR(50),
    customer_zip_code_prefix INTEGER,
    customer_city VARCHAR(50),
    customer_state VARCHAR(5)
);
CREATE TABLE order_items(
    order_id VARCHAR(50) PRIMARY KEY,
    order_item INTEGER,
    product_id VARCHAR(50),
    seller_id VARCHAR(50),
    shipping_limit_date DATE,
    price DECIMAL(10, 1),
    freight_value DECIMAL(10,1)
);
CREATE TABLE order_payments(
    order_id VARCHAR(50),
    payment_sequential INTEGER,
    payment_type_installments VARCHAR(100),
    payment_value DECIMAL(10, 2)
);
CREATE TABLE order_reviews(
    review_id VARCHAR(50),
    order_id VARCHAR(50),
    review_score INTEGER,
    review_comment_message TEXT
);
CREATE TABLE orders(
    customer_id VARCHAR(50),
    order_status VARCHAR(50),
    order_purchase_timestamp TIMESTAMP,
    order_approved_at TIMESTAMP,
    order_delivered_carrier_date TIMESTAMP,
    order_delivered_customer_date TIMESTAMP,
    order_estimated_delivery_date TIMESTAMP
);
CREATE TABLE sellers(
    seller_id VARCHAR(50),
    seller_zip_code_prefix INTEGER,
    seller_city VARCHAR(50),
    seller_state VARCHAR(5)
);
CREATE TABLE product_category_name_translation(
    product_category_name VARCHAR(100) UNIQUE PRIMARY KEY,
    product_category_name_english VARCHAR(100)
);
CREATE TABLE produts(
    product_id VARCHAR(50),
    product_category_name VARCHAR(100),
    product_name_length INTEGER,
    product_description_length INTEGER,
    product_photos_qty INTEGER,
    product_weight_g INTEGER,
    product_length_cm INTEGER,
    product_height_cm INTEGER,
    product_width_cm INTEGER,
);
CREATE TABLE geolocation(
    geolocation_zip_code_prefix INTEGER PRIMARY KEY,
    geolocation_lat FLOAT,
    geolocation_lng FLOAT,
    geolocation_city VARCHAR(50),
    geolocation_state VARCHAR(5)
);


