from datetime import datetime
from pydantic import BaseModel

class ItemModel(BaseModel):
    name: str
    email: str
    item_name: str
    quantity: int
    expiry_date: datetime
    insert_date: datetime = datetime.utcnow()
