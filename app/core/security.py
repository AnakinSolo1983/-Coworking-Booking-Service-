from datetime import datetime # import datetime from datetime
from datetime import timedelta # import timedelta from datetime

from jose import jwt # import jwt from jose
from passlib.context import CryptContext # import CryptContext from passlib.context

from app.core.config import settings # import settings from app.core.config


# create password context:
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# create hash_password function:
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# create verify_password function:
def verify_password(
    plain_password: str, # plain password
    hashed_password: str # hashed password
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# create create_access_token function:
def create_access_token(
    data: dict # data
) -> str:

    payload = data.copy() # copy data

    # set expire time:
    expire = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload["exp"] = expire # set expire time

    # encode payload:
    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )