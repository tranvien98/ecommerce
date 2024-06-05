from app.auth import schemas, services
from fastapi import APIRouter

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
