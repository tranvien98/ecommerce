from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, StringConstraints


class UserBase(BaseModel):
    user_name: str
    user_email: EmailStr
    full_name: str
    user_password: str

class UserInCreate(UserBase):
    user_name: str = Field(..., max_length=50, min_length=3, pattern="^[a-zA-Z0-9_]+$")
    user_email: EmailStr
    full_name: str
    user_password: str


class UserResponse(UserBase):
    user_name: str
    user_email: EmailStr
    full_name: str
    user_password: str
    user_status: str
    is_verified: bool
    user_roles: list[str]
    is_deleted: bool
    created_at: datetime
    updated_at: datetime
