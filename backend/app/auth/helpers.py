import bcrypt


def check_password(password: str, password_in_db: str) -> bool:
    password_bytes = bytes(password, "utf-8")
    password_in_db_bytes = bytes(password_in_db, "utf-8")
    return bcrypt.checkpw(password_bytes, password_in_db_bytes)
