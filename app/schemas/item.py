from pydantic import BaseModel
from datetime import date
from typing import Optional

class ItemCreate(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: date

class ItemUpdate(BaseModel):
    item_name: Optional[str]
    quantity: Optional[int]
    expiry_date: Optional[date]
