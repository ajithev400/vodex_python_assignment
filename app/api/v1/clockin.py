from fastapi import APIRouter
from app.schemas.clockin import ClockInSchema  # Make sure to create this Pydantic model
from app.crud.clockin import create_clockin, get_clockin  # Make sure to implement these CRUD functions

router = APIRouter()

@router.post("/")
async def create_clock_in(clockin_data: ClockInSchema):
    return await create_clockin(clockin_data)

@router.get("/{id}")
async def read_clock_in(id: str):
    return await get_clockin(id)

# Add other clock-in endpoints as required
