from pydantic import BaseModel
from datetime import datetime

class ClockInSchema(BaseModel):
    user_id : str
    email: str
    location: str
    insert_datetime: datetime = None 

    @classmethod
    def create(cls, user_id: str, email: str, location: str):
        return cls(
            user_id=user_id,
            email=email,
            location=location,
            insert_datetime=datetime.utcnow()
        )
