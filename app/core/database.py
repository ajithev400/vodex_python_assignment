from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None  # Global MongoDB client

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING)
    print("Connected to MongoDB")  # Add this print statement for debugging

async def close_mongo_connection():
    global client
    if client:
        client.close()
        print("Disconnected from MongoDB")

def get_database():
    if client is None:
        raise ConnectionError("MongoDB client is not initialized. Call connect_to_mongo first.")
    return client[settings.MONGO_DB_NAME]
