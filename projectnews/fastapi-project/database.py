from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# UPDATE your password exactly as you use to login in mysql -p
# If your password contains @ or ! you must URL encode
# Example: Root@9142  --> Root%409142

DB_URL = "mysql+pymysql://root:Root%409142@127.0.0.1:3306/fastapi_db"

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

