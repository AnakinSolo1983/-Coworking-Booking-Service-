from fastapi import APIRouter # import router from fastapi
from fastapi import Depends # import depends from fastapi
from fastapi import HTTPException # import http exception from fastapi

from sqlalchemy.orm import Session # import session from sqlalchemy

from app.core.database import get_db # import get_db from app.core.database
from app.core.security import create_access_token # import create_access_token from app.core.security

from fastapi.security import OAuth2PasswordRequestForm # import OAuth2PasswordRequestForm from fastapi.security
from app.schemas.auth import TokenResponse # import TokenResponse from app.schemas.auth
from pydantic import BaseModel # import BaseModel from pydantic


# create token response model:
class TokenResponse(BaseModel):
    access_token: str # access token
    token_type: str = "bearer" # token type

# import auth service from app.services.auth_service:
from app.services.auth_service import (
    AuthService # auth service
)

# create router for auth:
router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# create endpoint for login:
@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), # dependency for form data
    db: Session = Depends(get_db) # dependency for database session
):

    # create auth service:
    service = AuthService(db)

    # authenticate user:
    user = service.authenticate(
        form_data.username,
        form_data.password
    )

    # if user is not found, raise http exception:
    # if user is not found, raise http exception:
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    # create access token:
    token = create_access_token(
        {
            "sub": str(user.id),
            "role": user.role.value
        }
    )

    # return access token:
    return {
        "access_token": token,
        "token_type": "bearer"
    }