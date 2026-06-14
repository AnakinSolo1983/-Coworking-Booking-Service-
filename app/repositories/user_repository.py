from sqlalchemy import select # import select from sqlalchemy
from sqlalchemy.orm import Session # import Session from sqlalchemy.orm

from app.models.user import User # import User from app.models.user


# create UserRepository class:
class UserRepository:

    # initialize UserRepository:
    def __init__(self, db: Session): # db: Session
        
        self.db = db # self.db

    # get user by id:
    def get_by_id(self, user_id: int) -> User | None: # user_id: int

        return self.db.get(User, user_id) # get user by id

    # get user by username:
    def get_by_username(self, username: str) -> User | None: # username: str

        stmt = select(User).where(
            User.username == username
        )

        return self.db.scalar(stmt)

    # create user:
    def create(self, user: User) -> User: # user: User

        self.db.add(user) # add user
        self.db.commit() # commit
        self.db.refresh(user)

        return user