from app.users import users_dependences, users_exceptions, users_schemas, users_service
from fastapi import APIRouter, Depends, Response, status
from fastapi.encoders import jsonable_encoder

router = APIRouter()

@router.post("/users/sign-up", status_code=status.HTTP_201_CREATED)
async def create_user(user: users_schemas.UserInCreate = Depends(users_dependences.valid_create_user)):
    user_data = await users_service.create_user(user)
    return {
        "status": "success",
        "message": "User created",
        "data": user_data
    }
