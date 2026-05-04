# main.py
from fastapi import FastAPI
from database import get_db_connection
import pandas as pd

app = FastAPI(title="Loan Risk Prediction API", version="1.0")

# Initialize DB connection when the app starts
engine = get_db_connection()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Loan Risk Prediction MLOps API"}

@app.get("/test-db")
def test_database():
    if engine is None:
        return {"status": "Failed", "message": "Could not connect to database"}
    return {"status": "Success", "message": "Database connected securely!"}
