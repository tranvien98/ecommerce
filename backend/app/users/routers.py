from app.users import dependences, schemas, services
from fastapi import APIRouter, Depends, status

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/sign-up", status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserInCreate = Depends(dependences.valid_create_user)):
    user_data = await services.create_user(user)
    return {
        "status_code" :status.HTTP_201_CREATED,
        "message": "User created successfully",
        "data": user_data
    }


@router.get("", status_code=status.HTTP_200_OK)
async def get_all_users():
    users = await services.get_all_users()
    return {
        "status_code": status.HTTP_200_OK,
        "message": "Users retrieved successfully",
        "data": users
    }


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def get_user_by_id(user_id: str):
    user = await services.get_user_by_id(user_id)
    return {
        "status_code": status.HTTP_200_OK,
        "message": "User retrieved successfully",
        "data": user
    }

@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: str, user_data: schemas.UpdateUser):
    user = await services.update_user(user_id, user_data.model_dump())
    return {
        "status_code": status.HTTP_200_OK,
        "message": "User updated",
        "data": user
    }
