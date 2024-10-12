from fastapi import APIRouter, HTTPException
from app.schemas.user import UserSchema  # Make sure to create this Pydantic model
from app.crud.users import create_user, get_user  # Ensure these CRUD functions are implemented

router = APIRouter()

@router.post("/")
async def create_new_user(user_data: UserSchema):
    return await create_user(user_data)

@router.get("/{id}")
async def read_user(id: str):
    user = await get_user(id)
    
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user


