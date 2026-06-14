from fastapi import Depends # import Depends from fastapi
from fastapi import HTTPException # import HTTPException from fastapi
from fastapi import status # import status from fastapi

from fastapi.security import OAuth2PasswordBearer # import OAuth2PasswordBearer from fastapi.security

from jose import jwt # import jwt from jose
from jose import JWTError # import JWTError from jose

from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.core.database import get_db # import get_db from app.core.database
from app.core.config import settings # import settings from app.core.config

from app.models.user import User # import User from app.models.user
from app.models.user import UserRole # import UserRole from app.models.user


# create oauth2 scheme:
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login" # token url
)


# create get_current_user function:
def get_current_user(
    token: str = Depends(oauth2_scheme), # token
    db: Session = Depends(get_db) # database
):

    # create credentials exception:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, # status code
        detail="Could not validate credentials" # detail
    )

    try:

        # decode token:
        payload = jwt.decode(
            token, # token
            settings.SECRET_KEY, # secret key
            algorithms=[settings.ALGORITHM] # algorithm
        )

        user_id = payload.get("sub") # user id

    except JWTError:
        raise credentials_exception # raise credentials exception

    # get user from database:
    user = db.get(User, int(user_id)) # user

    # check if user exists:
    if not user:
        raise credentials_exception # raise credentials exception

    return user


# create admin_required function:
def admin_required(
    current_user: User = Depends(get_current_user) # current user
):

    # check if user is admin:
    if current_user.role != UserRole.ADMIN:

        # raise admin privileges required exception:
        raise HTTPException(
            status_code=403, # status code
            detail="Admin privileges required" # detail
        )

    return current_user