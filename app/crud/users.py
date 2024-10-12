from app.core.database import get_database
from app.schemas.user import UserSchema


async def create_user(user_data: UserSchema):
    
    db = get_database()
    result = await db.users.insert_one(user_data.dict())
    return {"id": str(result.inserted_id), **user_data.dict()}


async def get_user(user_id: str):
    db = get_database()
    user = await db.users.find_one({"_id": user_id})
    
    if user:
        user["_id"] = str(user["_id"])
    
    return user