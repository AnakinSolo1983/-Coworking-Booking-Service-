from pydantic import BaseModel # import BaseModel from pydantic


# create LoginRequest schema:
class LoginRequest(BaseModel): # BaseModel

    username: str # username
    password: str # password


# create TokenResponse schema:
class TokenResponse(BaseModel): # BaseModel

    access_token: str # access token
    token_type: str = "bearer"