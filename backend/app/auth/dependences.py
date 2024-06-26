from typing import Annotated

from fastapi import Header
from fastapi.exceptions import HTTPException

from app.auth.services import get_current_user as auth_get_current_user

async def get_current_user(Authorization: Annotated[str, Header()]):
    """
    Get current user
    """
    authorization = Authorization
    if authorization:
        try:
            schema, token = authorization.split()
            if schema.lower() != "bearer":
                raise HTTPException(status_code=401, detail="Invalid token1")
            user = await auth_get_current_user(token)
            return user
        except:
            raise HTTPException(status_code=401, detail="Invalid token2")
    else:
        raise HTTPException(status_code=401, detail="Invalid token3")
