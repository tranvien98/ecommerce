from jose import jwt
from datetime import datetime, timedelta
from beanie import PydanticObjectId

from app.auth.constants import ExpireTimes
from app.auth.exceptions import AuthError, InvalidPassword, UserNotActive
from app.auth.helpers import check_password
from app.auth.schemas import UserInSignIn
from app.core.config import settings
from app.users.models import Users

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/sign-in", auto_error=False)

async def authenticate_user(user_form: UserInSignIn):
    """
    Sign in a user
    """
    user = await Users.find_one(Users.user_name == user_form.user_name, Users.is_deleted == False)
    if user is None:
        raise InvalidPassword
    if not check_password(user_form.user_password, user.user_password):
        raise InvalidPassword
    if user.user_status == "inactive":
        raise UserNotActive
    return user


async def create_refresh_token(data: dict, refresh_token: str|None = None):
    """
    Create an refresh token for a user
    data: user info
    refresh_token: refresh token old
    """
    expires_delta = datetime.now() + timedelta(days=ExpireTimes.REFRESH_TOKEN)
    to_encode = data.copy()
    to_encode.update({"exp": expires_delta})
    to_encode.update({"version": settings.version})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def create_access_token(data: dict, refresh_token: str|None = None):
    """
    Create an access token for a user
    data: user info
    refresh_token: refresh token old
    """
    expires_delta = datetime.now() + timedelta(minutes=ExpireTimes.ACCESS_TOKEN)
    to_encode = data.copy()
    to_encode.update({"exp": expires_delta})
    to_encode.update({"version": settings.version})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt


async def get_current_user(token: str):
    """
    Get current user
    """
    if not token:
        return AuthError
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user = await Users.find_one(Users.id == PydanticObjectId(payload.get("user_id")))
        return user
    except:
        return None


async def verify_refresh_token(refresh_token: str):
    """
    Verify refresh token
    """
    try:
        payload = jwt.decode(refresh_token, settings.secret_key, algorithms=[settings.algorithm])
        return payload
    except:
        return None
