from pydantic import BaseModel, Field


class UserInSignIn(BaseModel):
    user_name: str = Field(..., max_length=50, min_length=3, pattern="^[a-zA-Z0-9_]+$")
    user_password: str = Field(..., min_length=3)
