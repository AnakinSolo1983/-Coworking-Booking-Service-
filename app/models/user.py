from enum import Enum # import Enum from enum

from sqlalchemy import String # import String from sqlalchemy
from sqlalchemy import Enum as SqlEnum # import Enum from sqlalchemy
from sqlalchemy.orm import Mapped # import Mapped from sqlalchemy.orm
from sqlalchemy.orm import mapped_column # import mapped_column from sqlalchemy.orm
from sqlalchemy.orm import relationship # import relationship from sqlalchemy.orm

from app.core.database import Base # import Base from app.core.database


# create UserRole enum:
class UserRole(str, Enum):

    ADMIN = "admin" # admin
    EMPLOYEE = "employee" # employee


# create User class:
class User(Base):

    __tablename__ = "users" # table name

    id: Mapped[int] = mapped_column(primary_key=True) # primary key

    # username:
    # username:
    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    # password hash:
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    # role:
    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole),
        nullable=False
    )

    # bookings relationship:
    bookings = relationship(
        "Booking", # booking
        back_populates="user", # back populates
        cascade="all, delete-orphan" # cascade
    )