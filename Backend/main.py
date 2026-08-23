import os
from dotenv import load_dotenv
from fastapi import FastAPI
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI(title="AGRISMART")


@app.get("/")
def root():
    return {"message": "AGRISMART Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}