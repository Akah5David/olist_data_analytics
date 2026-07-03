import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

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

print(orders.head())
print("\n Order Shape: ", orders.shape)
print("\n Order Shape: ", order_payments.shape)
print("\n Order Shape: ", order_items.shape)
print("\n Order Shape: ", order_reviews.shape)
print("\n Order Shape: ", customers.shape)
print("\n Order Shape: ", geolocation.shape)
print("\n Order Shape: ", product_category_name_translation.shape)
print("\n Order Shape: ", products.shape)
print("\n Order Shape: ", sellers.shape)
orders.info()

# orders.to_sql("orders", engine, if_exists="replace", index=False)