
from fastapi import FastAPI

app = FastAPI(
    title="MVP-ai API",
    description="AI-powered fitness form analysis"
)

@app.get("/")
def home():
    return {
        "app": "Movement Vision Performance AI",
        "status": "Backend initialized"
    }

@app.get("/health")
def health():
    return {"status": "ok"}
