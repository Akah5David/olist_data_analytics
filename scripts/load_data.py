import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

import os

print(os.getcwd())

#reads your .env file and makes its values available through os.getenv().it does not return the environment variables. It simply #loads them into the process's environment and returns a boolean (True or False).
load_dotenv() 

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/"
    f"{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

with engine.connect() as conn: # Automatically opens and closes the database connection (similar to try...finally)
    result = conn.execute(text("""SELECT version();"""))

    print("Connection is successful")
    print(result.scalar())

# converts csv to pandas DataFrame(consider it Excel spreedsheet in memory)
orders = pd.read_csv("data/raw/orders.csv") 
order_payments = pd.read_csv("data/raw/order_payments.csv")
order_items = pd.read_csv("data/raw/order_items.csv")
order_reviews = pd.read_csv("data/raw/order_reviews.csv") 
customers = pd.read_csv("data/raw/customers.csv")
geolocation = pd.read_csv("data/raw/geolocation.csv")
product_category_name_translation = pd.read_csv("data/raw/product_category_name_translation.csv")
products = pd.read_csv("data/raw/products.csv") 
sellers = pd.read_csv("data/raw/sellers.csv")


def check_primary_key(df, columns):
    """
    Check whether one or more columns uniquely identify each row.
    """
    duplicates = df.duplicated(subset=columns).sum()

    if duplicates == 0:
        print(f"✅ {columns} can serve as a primary key.")
    else:
        print(f"❌ {columns} contain {duplicates} duplicate(s).")

print(orders.head())
print("\n Order Shape: ", orders.shape)
orders.info()

# Missing values
missing = pd.DataFrame({
    "Missing": orders.isnull().sum(),
    "Percentage": (orders.isnull().sum()/len(orders)*100).round(2)
})

# Duplicate checks
check_primary_key(orders, ["order_id"])


print(order_payments.head())
print("\n order_payments Shape: ", order_payments.shape)
order_payments.info()

# Missing values
missing = pd.DataFrame({
    "Missing": order_payments.isnull().sum(),
    "Percentage": (order_payments.isnull().sum()/len(order_payments)*100).round(2)
})

# Duplicate checks
check_primary_key(order_payments, ["order_id"])


print(order_items.head())
print("\n order_items Shape: ", order_items.shape)
order_items.info()

# Missing values
missing = pd.DataFrame({
    "Missing": order_payments.isnull().sum(),
    "Percentage": (order_payments.isnull().sum()/len(order_payments)*100).round(2)
})

# Duplicate checks
check_primary_key(order_items, ["order_id"])


print(order_reviews.head())
print("\n order_reviews Shape: ", order_reviews.shape)
order_reviews.info()

# Missing values
missing = pd.DataFrame({
    "Missing": order_reviews.isnull().sum(),
    "Percentage": (order_reviews.isnull().sum()/len(order_reviews)*100).round(2)
})

# Duplicate checks
check_primary_key(order_reviews, ["review_id"])


print(customers.head())
print("\n customers Shape: ", customers.shape)
customers.info()

# Missing values
missing = pd.DataFrame({
    "Missing": customers.isnull().sum(),
    "Percentage": (customers.isnull().sum()/len(customers)*100).round(2)
})

# Duplicate checks
check_primary_key(customers, ["customer_id"])



print(geolocation.head())
print("\n geolocation Shape: ", geolocation.shape)
geolocation.info()

# Missing values
missing = pd.DataFrame({
    "Missing": geolocation.isnull().sum(),
    "Percentage": (geolocation.isnull().sum()/len(geolocation)*100).round(2)
})

# Duplicate checks
check_primary_key(geolocation, ["geolocation_zip_code_prefix", "geolocation_lat"]) #failed second normalisation so further spliting is needed
check_primary_key(geolocation, ["geolocation_lat"])




print(product_category_name_translation.head())
print("\n product_category_name_translation Shape: ", product_category_name_translation.shape)
product_category_name_translation.info()

# Missing values
missing = pd.DataFrame({
    "Missing": product_category_name_translation.isnull().sum(),
    "Percentage": (product_category_name_translation.isnull().sum()/len(product_category_name_translation)*100).round(2)
})

# Duplicate checks
check_primary_key(product_category_name_translation, ["product_category_name"])



print(products.head())
print("\n products Shape: ", products.shape)
products.info()

# Missing values
missing = pd.DataFrame({
    "Missing": products.isnull().sum(),
    "Percentage": (products.isnull().sum()/len(products)*100).round(2)
})

# Duplicate checks
check_primary_key(products, ["product_id"])



print(sellers.head())
print("\n sellers Shape: ", sellers.shape)
sellers.info()

# Missing values
missing = pd.DataFrame({
    "Missing": sellers.isnull().sum(),
    "Percentage": (sellers.isnull().sum()/len(sellers)*100).round(2)
})

# Duplicate checks
check_primary_key(sellers, ["seller_id"])





# orders.to_sql("orders", engine, if_exists="replace", index=False)