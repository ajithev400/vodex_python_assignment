from app.core.database import get_database  # Import the database connection
from app.schemas.clockin import ClockInSchema
from bson import ObjectId
from datetime import datetime
from fastapi import HTTPException

async def create_clockin(clockin_data: ClockInSchema):
    """Create a new clock-in record in the database."""
    db = get_database()
    clockin_dict = clockin_data.dict()
    
    # Set current time for insert_datetime if not provided
    if not clockin_dict.get("insert_datetime"):
        clockin_dict["insert_datetime"] = datetime.utcnow()
    
    # Insert the clock-in record into the MongoDB collection
    result = await db.clockin.insert_one(clockin_dict)
    return str(result.inserted_id)

async def get_clockin(clockin_id: str):
    """Retrieve a clock-in record by its ID."""
    db = get_database()
    
    # Validate the ObjectId format
    if not ObjectId.is_valid(clockin_id):
        raise HTTPException(status_code=400, detail="Invalid clock-in ID format.")
    
    # Retrieve the clock-in record
    record = await db.clockin.find_one({"_id": ObjectId(clockin_id)})
    
    if record:
        # Optionally, you can format the record before returning
        record["_id"] = str(record["_id"])  # Convert ObjectId to string for JSON serialization
        return record
    else:
        raise HTTPException(status_code=404, detail="Clock-in record not found.")
