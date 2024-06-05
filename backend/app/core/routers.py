from app.auth.routers import router as auth_api_router
from app.users.routers import router as users_api_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(auth_api_router, tags=["auth"])
router.include_router(users_api_router, tags=["users"])
