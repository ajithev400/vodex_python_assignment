from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_CONNECTION_STRING: str = "mongodb://localhost:27017"
    MONGO_DB_NAME: str = "mydatabase"

settings = Settings()
