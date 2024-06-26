from app.auth.services import get_current_user
from fastapi.responses import UJSONResponse
from starlette.middleware.base import BaseHTTPMiddleware


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        not_auth_routes = ["/api/sign-in", "/api/users/sign-up", "/api/refresh-token"]
        if request.url.path in not_auth_routes:
            response = await call_next(request)
            return response
        authorization = request.headers.get("Authorization")
        if authorization:
            try:
                schema, token = authorization.split()
                if schema.lower() != "bearer":
                    return UJSONResponse(content={"detail": "Invalid token"}, status_code=401)
                user = await get_current_user(token)
                request.state.user = user
                request.state.token = token
            except:
                return UJSONResponse(content={"detail": "Invalid token"}, status_code=401)
        else:
            return UJSONResponse(content={"detail": "Invalid token"}, status_code=401)
        response = await call_next(request)
        return response
