from typing import Any

from fastapi import HTTPException, status


class BaseHTTPException(HTTPException):
    STATUS_CODE: int = status.HTTP_500_INTERNAL_SERVER_ERROR
    DETAIL = "Server Error"
    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(status_code=self.STATUS_CODE, detail=self.DETAIL, **kwargs)


class NotFound(BaseHTTPException):
    STATUS_CODE = status.HTTP_404_NOT_FOUND
    DETAIL = "Not Found"


class BadRequest(BaseHTTPException):
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
    DETAIL = "Bad Request"

class Unauthorized(BaseHTTPException):
    STATUS_CODE = status.HTTP_401_UNAUTHORIZED
    DETAIL = "Unauthorized"

    def __init__(self, **kwargs: dict[str, Any]):
        super().__init__(headers={"WWW-Authenticate": "Bearer"}, **kwargs)
