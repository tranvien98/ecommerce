
class ErrorCodes:
    INVALID_PASSWORD = 'username or password is incorrect'
    USER_NOT_ACTIVE = 'user is not active'
    AUTH_REQUIRED = 'authentication required'


class ExpireTimes:
    ACCESS_TOKEN = 60 #minutes
    REFRESH_TOKEN = 7 # days
