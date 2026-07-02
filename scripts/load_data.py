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

orders = pd.read_csv("data/raw/orders.csv") # converts csv to pandas DataFrame(consider it Excel spreedsheet in memory)

print(orders.head())
print("\n Order Shape: ", orders.shape)
orders.info()

# orders.to_sql("orders", engine, if_exists="replace", index=False)