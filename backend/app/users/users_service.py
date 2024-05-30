from app.users.security import check_password, hash_password
from app.users.users_model import Users
from app.users.users_schemas import UserInCreate


async def create_user(user: UserInCreate):
    """
    Create a new user in the database
    """
    user = Users(**user.model_dump())
    user.user_password = hash_password(user.user_password)
    await user.insert()
    return user
