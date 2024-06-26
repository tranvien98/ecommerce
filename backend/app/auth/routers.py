from app.auth import schemas, services
from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/sign-in")
async def sign_in(user: schemas.UserInSignIn):
    user = await services.authenticate_user(user)
    data_encoded = {
        "user_id": str(user.id)
    }
    access_token = await services.create_access_token(data_encoded)
    refresh_token = await services.create_refresh_token(data_encoded)
    return {
        "status_code": 200,
        "message": "User signed in successfully",
        "data": {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    }


@router.post("/refresh-token")
async def refresh_token(refresh_token: str = Body(..., embed=True)):
    payload = await services.verify_refresh_token(refresh_token)
    data = {
        "user_id": payload["user_id"]
    }
    access_token = await services.create_access_token(data)
    refresh_token = await services.create_refresh_token(data)
    return {
        "status_code": 200,
        "message": "Token refreshed successfully",
        "data": {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    }
