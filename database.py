# database.py
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

def get_db_connection():
    """Test the database connection and return the engine."""
    try:
        with engine.connect() as connection:
            print("Successfully connected to the PostgreSQL database!")
        return engine
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
