from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def health_check():
    return {"status": "ok", "message": "Service is healthy"}

@router.get("/ping")
def ping():
    return {"ping": "pong"}
