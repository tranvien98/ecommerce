
from app.users.users_exceptions import EmailAlreadyExists, UsernameAlreadyExists
from app.users.users_model import Users
from app.users.users_schemas import UserInCreate


async def valid_create_user(user: UserInCreate):
    """
    Validate user creation
    """
    if await Users.find_one(Users.user_name==user.user_name, Users.is_deleted==False):
        raise UsernameAlreadyExists
    if await Users.find_one(Users.user_email==user.user_email, Users.is_deleted==False):
        raise EmailAlreadyExists

    return user
