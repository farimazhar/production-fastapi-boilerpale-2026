from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "My Awesome API"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
