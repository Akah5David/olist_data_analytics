from sqlalchemy import create_engine, text

engine  = create_engine(
"postgresql+psycopg2://olist_user:1999Davido@localhost:5432/olist"
)

# print(engine.connect())
with engine.connect() as conn: # automatically triggers the connection for you and prevents forgotten database connections
    result = conn.execute(text("""SELECT version();"""))

    print("✅ Connected successfully!")
    print(result.scalar())