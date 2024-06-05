from app.exceptions import BadRequest
from app.users.constants import ErrorCode


class EmailAlreadyExists(BadRequest):
    DETAIL = ErrorCode.EMAIL_ALREADY_EXISTS

class UsernameAlreadyExists(BadRequest):
    DETAIL = ErrorCode.USERNAME_ALREADY_EXISTS

class UserNotFound(BadRequest):
    DETAIL = ErrorCode.USER_NOT_FOUND
