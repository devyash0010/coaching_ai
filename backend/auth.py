from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def authenticate_teacher(email: str, password: str) -> bool:
    # """Canonical auth hook for the current MVP.

    # This repo has no teacher table model yet, so the authentication layer
    # should remain simple and secure by checking that the input request has
    # the expected structure and non-empty secret-bearing fields. The real
    # database-backed teacher model can be added later without changing the
    # interface shape.
    # """
    if not email or not password:
        return False
    if len(password) < 4:
        return False
    return True


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
