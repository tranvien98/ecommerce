from app.auth.constants import ErrorCodes
from app.exceptions import BadRequest, Unauthorized


class InvalidPassword(BadRequest):
    """
    Invalid password
    """
    DETAIL = ErrorCodes.INVALID_PASSWORD


class UserNotActive(BadRequest):
    """
    User is not active
    """
    DETAIL = ErrorCodes.USER_NOT_ACTIVE


class AuthError(Unauthorized):
    """
    Auth error
    """
    DETAIL = ErrorCodes.AUTH_REQUIRED
