from fastapi import FastAPI
from app.api.v1 import items, clockin, users
from app.core.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

# Event that runs when the app starts
@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

# Event that runs when the app shuts down
@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

# Include API routers
app.include_router(items.router, prefix="/api/v1/items", tags=["Items"])
app.include_router(clockin.router, prefix="/api/v1/clockin", tags=["Clock-In"])
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
