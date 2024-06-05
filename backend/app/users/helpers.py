import bcrypt


def hash_password(password: str) -> bytes:
    pw = bytes(password, "utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pw, salt)
    return str(hashed, "utf-8")
