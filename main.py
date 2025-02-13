from fastapi import FastAPI
import os  # Hier oben einfügen!
from sqlalchemy import create_engine

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Die API läuft!"}

# 📌 Datenbank-Verbindung
DATABASE_URL = os.getenv("DATABASE_URL")  # Holt die URL aus den Umgebungsvariablen
engine = create_engine(DATABASE_URL)

