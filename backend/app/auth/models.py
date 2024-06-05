from datetime import datetime

from beanie import Document
from pydantic import Field


class RefreshToken(Document):
    """
    RefreshToken model for refresh_tokens collection in database.
    """
    user_id: str
    refresh_token: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Settings:
        collection = "refresh_tokens"
