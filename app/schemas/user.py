from pydantic import BaseModel

class UserSchema(BaseModel):
    name: str
    email: str
    password: str  # or other user fields as needed

    class Config:
        orm_mode = True
