from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="Production FastAPI Boilerplate",
    description="A production-ready FastAPI boilerplate for 2026",
    version="1.0.0"
)

@app.get("/")
def root():
    """
    Root endpoint to check if API is running
    """
    return {
        "message": "API is running successfully",
        "status": "active",
        "docs": "/docs"
    }

@app.get("/health")
def health_check():
    """
    Health check endpoint for production monitoring
    """
    return {
        "status": "ok",
        "uptime": "100%"
    }

@app.get("/api/v1/hello")
def hello(name: str = "World"):
    """
    Example API endpoint
    """
    return {"hello": name}
