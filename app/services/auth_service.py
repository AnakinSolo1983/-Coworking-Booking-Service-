from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.core.security import verify_password # import verify_password from app.core.security

from app.repositories.user_repository import (
    UserRepository # import UserRepository from app.repositories.user_repository
)


# create AuthService class:
class AuthService:

    # initialize AuthService:
    def __init__(self, db: Session): # db: Session

        self.users = UserRepository(db) # self.users

    # authenticate user:
    def authenticate(
        self,
        username: str,
        password: str
    ): # username: str, password: str

        user = self.users.get_by_username(
            username
        ) # get user by username

        # if user not found, return None:
        if not user:
            return None

        # if password is not correct, return None:
        if not verify_password(
            password,
            user.password_hash
        ): # verify password
            return None

        return user # return user