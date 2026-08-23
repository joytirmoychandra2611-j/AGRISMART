import os
from dotenv import load_dotenv
from fastapi import FastAPI
from supabase import create_client, Client
from weather import get_weather

# Load environment variables
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Create FastAPI app
app = FastAPI(title="AGRISMART")


@app.get("/")
def root():
    return {"message": "AGRISMART Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.get("/weather")
def weather(city: str):
    return get_weather(city)