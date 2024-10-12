from app.models.item import ItemModel
from app.schemas.item import ItemCreate
from app.core.database import get_database
from bson import ObjectId
from datetime import datetime,date




async def create_item(item_data: ItemCreate):
    db = get_database()

    # Convert Pydantic model to dictionary
    item_dict = item_data.dict()

    # Convert expiry_date (date) to datetime
    item_dict["expiry_date"] = datetime.combine(item_dict["expiry_date"], datetime.min.time())
    
    # Add the current insert date
    item_dict["insert_date"] = datetime.now()

    # Insert the item into MongoDB
    result = await db.items.insert_one(item_dict)

    # Return the inserted document's ID as a string
    return str(result.inserted_id)

async def get_item_by_id(id: str):
    db = get_database()

    # Find the item by ID
    item = await db.items.find_one({"_id": ObjectId(id)})
    
    if item:
        item["_id"] = str(item["_id"])
    
    return item

async def update_item(id: str, item_data: dict):
    db = get_database()

    # Check if "expiry_date" is in the item data and is a date object
    if "expiry_date" in item_data and isinstance(item_data["expiry_date"], date):
        # Convert date to datetime for MongoDB storage
        item_data["expiry_date"] = datetime.combine(item_data["expiry_date"], datetime.min.time())
    
    # Add a modification timestamp
    item_data["update_date"] = datetime.now()

    # Perform the update in MongoDB
    result = await db.items.update_one({"_id": ObjectId(id)}, {"$set": item_data})

    if result.modified_count == 1:
        return {"status": "success", "message": "Item updated successfully."}
    else:
        return {"status": "error", "message": "Item update failed."}
    
async def delete_item(id: str):
    db = get_database()

    # Delete the item from MongoDB
    await db.items.delete_one({"_id": ObjectId(id)})



