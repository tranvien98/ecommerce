from app.users.users_router import router as users_api_router
from fastapi import APIRouter

router = APIRouter()

router.include_router(users_api_router, tags=["users"])
