from datetime import datetime
from typing import Literal

from beanie import Document, Indexed
from pydantic import Field


class Users(Document):
    """
    Users model for users collection in database.
    """
    user_name:str = Indexed(unique=True)
    user_email:str = Indexed(unique=True)
    full_name:str
    user_password:str
    user_status: Literal["active", "inactive"] = "active"
    is_verified: bool = False
    user_roles: list[str] = []
    is_deleted: bool = False
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        collection = "users"
        indexes = ["user_name", "user_email"]
