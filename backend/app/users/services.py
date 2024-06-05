from beanie import PydanticObjectId

from app.users.exceptions import UserNotFound
from app.users.helpers import hash_password
from app.users.models import Users
from app.users.schemas import UserInCreate


async def create_user(user: UserInCreate):
    """
    Create a new user in the database
    """
    user = Users(**user.model_dump())
    user.user_password = hash_password(user.user_password)
    await user.insert()
    return user


async def get_all_users():
    """
    Get all users from the database
    """
    users = await Users.find(Users.is_deleted == False).to_list()
    return users


async def get_user_by_id(user_id: str):
    """
    Get a user by its ID from the database
    """
    user = await Users.find_one(Users.id == PydanticObjectId(user_id))
    if user is None:
        raise UserNotFound
    return user


async def update_user(user_id: str, user_data: dict):
    """
    Update a user in the database
    """
    user_data = {k: v for k, v in user_data.items() if v is not None}
    user = await get_user_by_id(user_id)
    if user is None:
        raise UserNotFound

    if "user_password" in user_data:
        user_data["user_password"] = hash_password(user_data["user_password"])

    await user.set(user_data)
    return user
