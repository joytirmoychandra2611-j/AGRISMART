from fastapi import FastAPI

app = FastAPI(title="AGRISMART")


@app.get("/")
def root():
    return {"message": "AGRISMART Backend is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}