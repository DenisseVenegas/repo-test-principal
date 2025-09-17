from fastapi import FastAPI
import psycopg2
import os

# uvicorn app.main:app --reload

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
API_KEY = os.getenv("API_KEY")

@app.get("/")
def root():
    return {"message": "FastAPI with PostgreSQL test"}


@app.get("/status")
def status():
    try:
        conn = psycopg2.connect(DATABASE_URL)
        conn.close()
        return {"status": "Database connection successful"}
    except Exception as e:
        return {"status": "Database connection failed", "error": str(e)}
    

@app.get("/apikey")
def get_api_key():
    if API_KEY:
        return {"api_key": API_KEY}
    else:
        return {"error": "API key not set"}
    

